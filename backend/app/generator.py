# -*- coding: utf-8 -*-
"""Weekly plan generator for Sedmica."""
import math
import random
from .data import RECIPES, ING_BY_ID, STORES

DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
MEALS = ["breakfast", "lunch", "dinner"]

STORE_MULT = {s["id"]: s["mult"] for s in STORES}


def _blocked(recipe, allergies, stops):
    stops_l = [s.strip().lower() for s in stops if s.strip()]
    for ing_id in recipe["ings"]:
        ing = ING_BY_ID[ing_id]
        if set(ing["allergens"]) & set(allergies):
            return True
        hay = (ing["ru"] + " " + ing["sr"] + " " + " ".join(ing["stop"])).lower()
        for s in stops_l:
            if s and s in hay:
                return True
        name_hay = (recipe["ru"] + " " + recipe["sr"]).lower()
        for s in stops_l:
            if s and s in name_hay:
                return True
    return False


def _available(recipe, store):
    for ing_id in recipe["ings"]:
        if store in ING_BY_ID[ing_id].get("not_in", []):
            return False
    return True


def _equip_ok(recipe, equipment):
    eq = set(equipment)
    for group in recipe["equip"]:
        if not group:
            continue
        if not (eq & set(group)):
            return False
    return True


def candidates(meal, allergies, stops, equipment, store="maxi"):
    return [r for r in RECIPES
            if r["meal"] == meal
            and _equip_ok(r, equipment)
            and _available(r, store)
            and not _blocked(r, allergies, stops)]


def recipe_cost(recipe, servings, store):
    """Marginal cost: price per gram/unit * qty (ignores pack rounding for ranking)."""
    mult = STORE_MULT.get(store, 1.0)
    total = 0.0
    for ing_id, qty in recipe["ings"].items():
        ing = ING_BY_ID[ing_id]
        total += ing["price"] * mult / ing["pack"] * qty * servings
    return total


def build_week(meal_pools, servings_map, store, rng):
    """Pick 7x3 avoiding repeats; returns {day: {meal: recipe_id}}."""
    week = {}
    used_counts = {}
    last_by_meal = {m: None for m in MEALS}
    for d in DAYS:
        week[d] = {}
        for m in MEALS:
            pool = meal_pools[m]
            if not pool:
                week[d][m] = None
                continue
            # prefer least-used, avoid same as yesterday
            best = sorted(pool, key=lambda r: (used_counts.get(r["id"], 0),
                                               1 if last_by_meal[m] == r["id"] else 0,
                                               rng.random()))
            pick = best[0]
            week[d][m] = pick["id"]
            used_counts[pick["id"]] = used_counts.get(pick["id"], 0) + 1
            last_by_meal[m] = pick["id"]
    return week


def shopping_from_week(week, servings_map, store):
    """Aggregate ingredient qty -> packs -> cost."""
    mult = STORE_MULT.get(store, 1.0)
    need = {}
    for d in DAYS:
        for m in MEALS:
            rid = week[d].get(m)
            if not rid:
                continue
            r = next(x for x in RECIPES if x["id"] == rid)
            servings = servings_map["family"] if r["family"] else servings_map[m]
            for ing_id, qty in r["ings"].items():
                need[ing_id] = need.get(ing_id, 0.0) + qty * servings
    items = []
    total = 0
    for ing_id, qty in sorted(need.items(), key=lambda kv: ING_BY_ID[kv[0]]["cat"]):
        ing = ING_BY_ID[ing_id]
        packs = max(1, math.ceil(qty / ing["pack"] - 0.02))
        price = round(ing["price"] * mult / 10) * 10 if ing["price"] > 200 else round(ing["price"] * mult)
        cost = price * packs
        total += cost
        items.append({
            "id": ing_id, "ru": ing["ru"], "sr": ing["sr"], "cat": ing["cat"],
            "packs": packs, "lab_ru": ing["lab_ru"], "lab_sr": ing["lab_sr"],
            "qty": round(qty), "unit": ing["unit"], "cost": cost,
        })
    return items, total


def day_costs(week, servings_map, store):
    """Approximate per-day marginal cost (for day cards)."""
    out = {}
    for d in DAYS:
        c = 0.0
        kcal = 0
        meals = {}
        for m in MEALS:
            rid = week[d].get(m)
            if not rid:
                continue
            r = next(x for x in RECIPES if x["id"] == rid)
            servings = servings_map["family"] if r["family"] else servings_map[m]
            mc = recipe_cost(r, servings, store)
            c += mc
            kcal += r["kcal"]
            meals[m] = {"id": r["id"], "ru": r["ru"], "sr": r["sr"], "emoji": r["emoji"], "icon": r.get("icon", "stew"),
                        "time": r["time"], "kcal": r["kcal"], "servings": servings,
                        "family": r["family"], "cost": round(mc / 10) * 10}
        out[d] = {"cost": round(c / 10) * 10, "kcal": kcal, "meals": meals}
    return out


def generate(params):
    """params: store, people, budget, allergies[], stops[], equipment[], seed?"""
    rng = random.Random(params.get("seed"))
    people = max(1, min(8, int(params.get("people", 2))))
    budget = int(params.get("budget", 8000))
    store = params.get("store", "maxi")
    allergies = params.get("allergies", [])
    stops = params.get("stops", [])
    equipment = params.get("equipment", ["stove"])

    servings_map = {"breakfast": people, "lunch": people, "dinner": people, "family": people}

    pools = {m: candidates(m, allergies, stops, equipment, store) for m in MEALS}
    for m in MEALS:
        if not pools[m]:
            pools[m] = [r for r in RECIPES if r["meal"] == m and _equip_ok(r, equipment) and _available(r, store)]
        if not pools[m]:
            pools[m] = [r for r in RECIPES if r["meal"] == m]

    week = build_week(pools, servings_map, store, rng)
    items, total = shopping_from_week(week, servings_map, store)

    # fit budget: greedy single-meal swaps, accept only real improvements of the
    # pack-aware total (swapping can add packs, so evaluate the actual basket)
    guard = 0
    while total > budget and guard < 25:
        guard += 1
        best = None  # (new_total, d, m, rid)
        for d in DAYS:
            for m in MEALS:
                cur = week[d].get(m)
                if not cur:
                    continue
                for cand in pools[m]:
                    if cand["id"] == cur:
                        continue
                    week[d][m] = cand["id"]
                    _, t2 = shopping_from_week(week, servings_map, store)
                    if t2 < total and (best is None or t2 < best[0]):
                        best = (t2, d, m, cand["id"])
                week[d][m] = cur
        if not best:
            break
        _, d, m, rid = best
        week[d][m] = rid
        items, total = shopping_from_week(week, servings_map, store)

    days = day_costs(week, servings_map, store)
    return {
        "params": {"store": store, "people": people, "budget": budget,
                   "allergies": allergies, "stops": stops, "equipment": equipment},
        "week": week, "days": days, "shopping": items,
        "total": total, "left": max(0, budget - total),
        "positions": len(items),
        "kcal_day": round(sum(days[d]["kcal"] for d in DAYS) / 7),
    }


def swap_meal(plan, day, meal):
    """Replace one meal with a different candidate, cheapest-first bias."""
    p = plan["params"]
    rng = random.Random()
    pools = candidates(meal, p["allergies"], p["stops"], p["equipment"], p["store"])
    current = plan["week"][day].get(meal)
    options = [r for r in pools if r["id"] != current]
    if not options:
        return plan
    used = {plan["week"][d][m] for d in DAYS for m in MEALS if plan["week"][d].get(m)}
    fresh = [r for r in options if r["id"] not in used]
    pick = rng.choice(fresh or options)
    plan["week"][day][meal] = pick["id"]
    servings_map = {"breakfast": p["people"], "lunch": p["people"], "dinner": p["people"], "family": p["people"]}
    items, total = shopping_from_week(plan["week"], servings_map, p["store"])
    days = day_costs(plan["week"], servings_map, p["store"])
    plan.update({"shopping": items, "total": total, "left": max(0, p["budget"] - total),
                 "days": days, "positions": len(items),
                 "kcal_day": round(sum(days[d]["kcal"] for d in DAYS) / 7)})
    return plan
