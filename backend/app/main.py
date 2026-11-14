# -*- coding: utf-8 -*-
import json
import os
import secrets
import sqlite3
from contextlib import closing

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from .data import STORES, CITIES, ALLERGENS, EQUIPMENT, STOP_SUGGESTIONS, CATS, RECIPES, ING_BY_ID
from .generator import generate, swap_meal, DAYS, MEALS

DB_PATH = os.environ.get("SEDMICA_DB", os.path.join(os.path.dirname(__file__), "..", "sedmica.db"))

app = FastAPI(title="Sedmica API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS plans (token TEXT PRIMARY KEY, data TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
    return conn


class GenerateReq(BaseModel):
    store: str = "maxi"
    city: str = "Beograd"
    people: int = Field(2, ge=1, le=8)
    budget: int = Field(8000, ge=1000, le=100000)
    allergies: list[str] = []
    stops: list[str] = []
    equipment: list[str] = ["stove"]


@app.get("/api/meta")
def meta():
    return {"stores": STORES, "cities": CITIES, "allergens": ALLERGENS,
            "equipment": EQUIPMENT, "stops": STOP_SUGGESTIONS, "cats": CATS}


@app.post("/api/plan")
def create_plan(req: GenerateReq):
    plan = generate(req.model_dump())
    plan["params"]["city"] = req.city
    token = secrets.token_urlsafe(8)
    with closing(db()) as conn:
        conn.execute("INSERT INTO plans (token, data) VALUES (?, ?)", (token, json.dumps(plan, ensure_ascii=False)))
        conn.commit()
    return {"token": token, "plan": plan}


@app.get("/api/plan/{token}")
def get_plan(token: str):
    with closing(db()) as conn:
        row = conn.execute("SELECT data FROM plans WHERE token=?", (token,)).fetchone()
    if not row:
        raise HTTPException(404, "plan not found")
    return {"token": token, "plan": json.loads(row[0])}


class SwapReq(BaseModel):
    day: str
    meal: str


@app.post("/api/plan/{token}/swap")
def swap(token: str, req: SwapReq):
    if req.day not in DAYS or req.meal not in MEALS:
        raise HTTPException(400, "bad day/meal")
    with closing(db()) as conn:
        row = conn.execute("SELECT data FROM plans WHERE token=?", (token,)).fetchone()
        if not row:
            raise HTTPException(404, "plan not found")
        plan = swap_meal(json.loads(row[0]), req.day, req.meal)
        conn.execute("UPDATE plans SET data=? WHERE token=?", (json.dumps(plan, ensure_ascii=False), token))
        conn.commit()
    return {"token": token, "plan": plan}


@app.get("/api/recipe/{rid}")
def recipe(rid: str):
    r = next((x for x in RECIPES if x["id"] == rid), None)
    if not r:
        raise HTTPException(404, "recipe not found")
    ings = [{"id": k, "ru": ING_BY_ID[k]["ru"], "sr": ING_BY_ID[k]["sr"],
             "qty": v, "unit": ING_BY_ID[k]["unit"]} for k, v in r["ings"].items()]
    return {**r, "ingredients": ings}


# --- static frontend (production) ---
DIST = os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "dist")
if os.path.isdir(DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(DIST, "assets")), name="assets")

    @app.get("/{path:path}")
    def spa(path: str):
        full = os.path.join(DIST, path)
        if path and os.path.isfile(full):
            return FileResponse(full)
        return FileResponse(os.path.join(DIST, "index.html"),
                            headers={"Cache-Control": "no-cache, no-store, must-revalidate"})
