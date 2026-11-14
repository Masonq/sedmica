import { useEffect, useMemo, useRef, useState } from "react";
import { T, plural, fmt, CAT_KEY } from "./i18n.js";
import Icon from "./Icons.jsx";

const API = "/api";
const DAY_IDS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const MEAL_ORDER = ["breakfast", "lunch", "dinner"];
const MEAL_ICON = { breakfast: "sunrise", lunch: "sunhigh", dinner: "moon" };
const STORE_COLORS = {
  lidl: "#0050aa", maxi: "#d6001c", idea: "#e2001a", univer: "#00704a",
  dis: "#f07d00", aroma: "#7a1f7a", roda: "#c8102e", tempo: "#0072bc",
};

async function api(path, opts) {
  const r = await fetch(API + path, opts);
  if (!r.ok) throw new Error("api " + r.status);
  return r.json();
}

function useCountUp(target, dur = 700, fromZero = false) {
  const [v, setV] = useState(fromZero ? 0 : target);
  const ref = useRef(fromZero ? 0 : target);
  useEffect(() => {
    const from = ref.current, to = target;
    if (from === to) return;
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) { ref.current = to; setV(to); return; }
    const t0 = performance.now();
    let raf;
    const tick = (now) => {
      const p = Math.min(1, (now - t0) / dur);
      const e = 1 - Math.pow(1 - p, 3);
      setV(Math.round(from + (to - from) * e));
      if (p < 1) raf = requestAnimationFrame(tick);
      else ref.current = to;
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [target, dur]);
  return v;
}

function Confetti() {
  const parts = useMemo(() => Array.from({ length: 22 }, (_, i) => ({
    left: 4 + Math.random() * 92,
    delay: Math.random() * 0.45,
    dur: 1.3 + Math.random() * 0.9,
    color: ["#ff6b3d", "#e8a23d", "#ff8a60", "#f5f3f1", "#f5511e"][i % 5],
    rot: Math.random() * 360,
    size: 6 + Math.random() * 5,
  })), []);
  return (
    <div className="confetti" aria-hidden="true">
      {parts.map((p, i) => (
        <i key={i} style={{
          left: `${p.left}%`, animationDelay: `${p.delay}s`, animationDuration: `${p.dur}s`,
          background: p.color, width: p.size, height: p.size * 0.55,
          transform: `rotate(${p.rot}deg)`,
        }} />
      ))}
    </div>
  );
}

function useLocal(key, init) {
  const [v, setV] = useState(() => {
    try { const s = localStorage.getItem(key); return s !== null ? JSON.parse(s) : init; }
    catch { return init; }
  });
  useEffect(() => { try { localStorage.setItem(key, JSON.stringify(v)); } catch {} }, [key, v]);
  return [v, setV];
}

export default function App() {
  const [lang, setLang] = useLocal("sed_lang", navigator.language?.startsWith("ru") ? "ru" : "sr");
  const [theme, setTheme] = useLocal("sed_theme", "dark");
  const t = T[lang];
  useEffect(() => { document.documentElement.dataset.theme = theme; }, [theme]);
  useEffect(() => { document.documentElement.lang = lang; }, [lang]);

  const [meta, setMeta] = useState(null);
  const [screen, setScreen] = useState("landing"); // landing | wizard | building | plan | day | shop | error
  const [step, setStep] = useState(0);
  const [dayIdx, setDayIdx] = useState(0);
  const [toast, setToast] = useState("");
  const [recipe, setRecipe] = useState(null); // {data, servings}

  // wizard state
  const [city, setCity] = useState("Beograd");
  const [store, setStore] = useState("maxi");
  const [people, setPeople] = useState(2);
  const [budget, setBudget] = useState(8000);
  const [allergies, setAllergies] = useState([]);
  const [stops, setStops] = useState([]);
  const [stopInput, setStopInput] = useState("");
  const [equipment, setEquipment] = useState(["stove", "oven", "micro"]);

  const [token, setToken] = useLocal("sed_token", null);
  const [plan, setPlan] = useState(null);
  const [checked, setChecked] = useLocal("sed_checked", {});

  useEffect(() => { api("/meta").then(setMeta).catch(() => {}); }, []);

  useEffect(() => {
    const m = location.hash.match(/^#\/p\/([\w-]+)/);
    const tok = m ? m[1] : null;
    if (tok) {
      api(`/plan/${tok}`).then(({ plan }) => { setToken(tok); setPlan(plan); setScreen("plan"); }).catch(() => {});
    } else if (token) {
      api(`/plan/${token}`).then(({ plan }) => { setPlan(plan); }).catch(() => {});
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function showToast(msg) { setToast(msg); setTimeout(() => setToast(""), 1800); }

  async function build() {
    setScreen("building");
    const started = Date.now();
    try {
      const { token: tok, plan: p } = await api("/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ store, city, people, budget, allergies, stops, equipment }),
      });
      const wait = Math.max(0, 2600 - (Date.now() - started));
      setTimeout(() => {
        setToken(tok); setPlan(p); setChecked({});
        history.replaceState(null, "", `#/p/${tok}`);
        setScreen("plan");
      }, wait);
    } catch {
      setScreen("error");
    }
  }

  async function swap(day, meal) {
    try {
      const before = plan?.week?.[day]?.[meal];
      const { plan: p } = await api(`/plan/${token}/swap`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ day, meal }),
      });
      setPlan(p);
      if (before && p.week[day][meal] === before) showToast(t.noSwap);
    } catch { showToast(t.error); }
  }

  async function openRecipe(rid, servings) {
    try {
      const data = await api(`/recipe/${rid}`);
      setRecipe({ data, servings });
    } catch { showToast(t.error); }
  }

  const storeName = useMemo(() => {
    if (!meta || !plan) return "";
    return meta.stores.find((s) => s.id === plan.params.store)?.name ?? "";
  }, [meta, plan]);

  return (
    <div className="shell">
      <header className="topbar">
        <button className="brand" onClick={() => setScreen(plan ? "plan" : "landing")} aria-label="Sedmica">
          <span className="seven">7</span>Sedmica
        </button>
        <div className="topbar-actions">
          <button className="iconbtn" onClick={() => setLang(lang === "sr" ? "ru" : "sr")} aria-label="Language">
            {lang === "sr" ? "RU" : "SR"}
          </button>
          <button className="iconbtn" onClick={() => {
            document.documentElement.classList.add("tswitch");
            setTimeout(() => document.documentElement.classList.remove("tswitch"), 450);
            setTheme(theme === "dark" ? "light" : "dark");
          }} aria-label="Theme">
            <Icon name={theme === "dark" ? "sun" : "moon"} size={19} />
          </button>
        </div>
      </header>
      {screen === "landing" && (
        <Landing t={t} meta={meta} city={city} setCity={setCity}
          onStart={() => { setStep(0); setScreen("wizard"); }} />
      )}
      {screen === "wizard" && (
        <Wizard t={t} lang={lang} meta={meta} step={step} setStep={setStep}
          store={store} setStore={setStore} people={people} setPeople={setPeople}
          budget={budget} setBudget={setBudget} allergies={allergies} setAllergies={setAllergies}
          stops={stops} setStops={setStops} stopInput={stopInput} setStopInput={setStopInput}
          equipment={equipment} setEquipment={setEquipment}
          onBack={() => (step === 0 ? setScreen("landing") : setStep(step - 1))}
          onBuild={build} />
      )}
      {screen === "building" && <Building t={t} />}
      {screen === "plan" && plan && (
        <PlanView t={t} plan={plan} storeName={storeName}
          onDay={(i) => { setDayIdx(i); setScreen("day"); }}
          onShop={() => setScreen("shop")}
          onNew={() => { setScreen("wizard"); setStep(0); }}
          onShare={async () => {
            const url = `${location.origin}/#/p/${token}`;
            try {
              if (navigator.share) await navigator.share({ title: "Sedmica", url });
              else { await navigator.clipboard.writeText(url); showToast(t.copied); }
            } catch {}
          }} />
      )}
      {screen === "day" && plan && (
        <DayView t={t} lang={lang} plan={plan} dayIdx={dayIdx} setDayIdx={setDayIdx}
          onBack={() => setScreen("plan")} onSwap={swap} onOpen={openRecipe} />
      )}
      {screen === "shop" && plan && (
        <ShopView t={t} lang={lang} plan={plan} checked={checked} setChecked={setChecked}
          onBack={() => setScreen("plan")} />
      )}
      {screen === "error" && (
        <div className="errbox">
          <div className="e"><Icon name="salad" size={44} /></div>
          <p>{t.error}</p>
          <button className="cta" style={{ maxWidth: 260, margin: "20px auto 0" }} onClick={() => setScreen("wizard")}>
            {t.retry}
          </button>
        </div>
      )}
      {recipe && <RecipeSheet t={t} lang={lang} recipe={recipe} onClose={() => setRecipe(null)} />}
      {toast && <div className="toast">{toast}</div>}
    </div>
  );
}

/* ---------------- Landing ---------------- */
function Landing({ t, meta, city, setCity, onStart }) {
  const week = ["pancakes", "soup", "fish", "stew", "pasta", "chicken", "pie"];
  return (
    <main className="hero">
      <h1>
        {t.heroTitle.split("\n")[0]}{"\n"}
        <span className="hl">{t.heroTitle.split("\n")[1]}</span>
      </h1>
      <p>{t.heroSub}</p>
      <div className="week-strip photo" aria-hidden="true">
        {t.daysShort.map((d, i) => (
          <div className="cell" key={d} style={{ backgroundImage: `url(${dishPhoto(week[i])})` }}>
            <span className="d">{d}</span>
          </div>
        ))}
      </div>
      <div className="field">
        <label htmlFor="city">{t.cityLabel}</label>
        <div className="select-wrap">
          <select id="city" value={city} onChange={(e) => setCity(e.target.value)}>
            {(meta?.cities ?? ["Beograd"]).map((c) => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
      </div>
      <button className="cta" onClick={onStart}>{t.start}</button>
      <div className="hint-center">{t.free}</div>
    </main>
  );
}

/* ---------------- Wizard ---------------- */
function Wizard(props) {
  const { t, step, setStep, onBack, onBuild } = props;
  const total = 6;
  const titles = [
    [t.s1t, t.s1s], [t.s2t, t.s2s], [t.s3t, t.s3s],
    [t.s4t, t.s4s], [t.s5t, t.s5s], [t.s6t, t.s6s],
  ];
  const canNext =
    step === 0 ? !!props.store :
    step === 5 ? props.equipment.length > 0 : true;

  return (
    <main className="step" key={step}>
      <div className="progress" aria-hidden="true">
        {Array.from({ length: total }, (_, i) => <i key={i} className={i <= step ? "on" : ""} />)}
      </div>
      <div className="stephead">
        <button className="backbtn" onClick={onBack}>‹ {t.back}</button>
        <span className="label">{t.stepOf(step + 1, total)}</span>
      </div>
      <h2>{titles[step][0]}</h2>
      <p className="sub">{titles[step][1]}</p>
      <div className="step-body">
        {step === 0 && <StepStore {...props} />}
        {step === 1 && <StepPeople {...props} />}
        {step === 2 && <StepBudget {...props} />}
        {step === 3 && <StepAllergy {...props} />}
        {step === 4 && <StepStops {...props} />}
        {step === 5 && <StepEquip {...props} />}
      </div>
      <div className="step-foot">
        {step < total - 1 ? (
          <button className="cta" disabled={!canNext} onClick={() => setStep(step + 1)}>{t.next}</button>
        ) : (
          <button className="cta" disabled={!canNext} onClick={onBuild}>{t.build}</button>
        )}
      </div>
    </main>
  );
}

function StepStore({ meta, store, setStore, lang }) {
  const stores = meta?.stores ?? [];
  return (
    <div className="grid2">
      {stores.map((s, i) => (
        <button key={s.id} className={`tile ${store === s.id ? "on" : ""}`} onClick={() => setStore(s.id)}>
          {store === s.id && <span className="check"><Icon name="check" size={12} stroke={3} /></span>}
          <span className="logo" style={{ background: STORE_COLORS[s.id] ?? "#666" }}>{s.name[0]}</span>
          <span className="t">{s.name}</span>
          <span className="s">{lang === "ru" ? s.tag_ru : s.tag_sr}</span>
          {i === 0 && <span className="badge-reco">{lang === "ru" ? "выгоднее" : "najpovoljnije"}</span>}
        </button>
      ))}
    </div>
  );
}

function StepPeople({ t, people, setPeople }) {
  return (
    <div>
      <div className="stepper">
        <button className="sbtn" onClick={() => setPeople(Math.max(1, people - 1))} disabled={people <= 1} aria-label="−">
          <Icon name="minus" size={22} />
        </button>
        <span className="num">{people}</span>
        <button className="sbtn" onClick={() => setPeople(Math.min(8, people + 1))} disabled={people >= 8} aria-label="+">
          <Icon name="plus" size={22} />
        </button>
      </div>
      <div className="stepper-sub">{plural(people, t.persons)}</div>
    </div>
  );
}

function StepBudget({ t, people, budget, setBudget }) {
  const min = 3000, max = 30000;
  const fill = ((budget - min) / (max - min)) * 100;
  const shown = useCountUp(budget, 260);
  const perHead = budget / people;
  const mood = perHead < 2600 ? ["var(--red)", t.moodTight, t.moodTightS]
    : perHead < 4200 ? ["var(--green)", t.moodOk, t.moodOkS]
    : ["var(--amber)", t.moodSpare, t.moodSpareS];
  return (
    <div>
      <div className="budget-big">{fmt(shown)}<small>{t.cur}</small></div>
      <div className="budget-per">{t.perPerson(fmt(perHead))}</div>
      <input type="range" min={min} max={max} step={250} value={budget}
        style={{ "--fill": `${fill}%` }}
        onChange={(e) => setBudget(+e.target.value)} aria-label={t.s3t} />
      <div className="range-ends"><span>{fmt(min)}</span><span>{fmt(max)}</span></div>
      <div className="mood">
        <span className="dot" style={{ background: mood[0] }} />
        <span>
          <span className="mt">{mood[1]}</span>
          <span className="ms" style={{ display: "block" }}>{mood[2]}</span>
        </span>
      </div>
    </div>
  );
}

function StepAllergy({ t, lang, meta, allergies, setAllergies }) {
  const list = meta?.allergens ?? [];
  const toggle = (id) => setAllergies(allergies.includes(id) ? allergies.filter((x) => x !== id) : [...allergies, id]);
  return (
    <div>
      <div className="grid3">
        {list.map((a) => (
          <button key={a.id} className={`tile ${allergies.includes(a.id) ? "on" : ""}`} onClick={() => toggle(a.id)}>
            {allergies.includes(a.id) && <span className="check"><Icon name="check" size={12} stroke={3} /></span>}
            <span className="ticon"><Icon name={a.id} size={26} /></span>
            <span className="t" style={{ fontSize: 13 }}>{lang === "ru" ? a.ru : a.sr}</span>
          </button>
        ))}
      </div>
      {allergies.length > 0 && (
        <div className="chips">
          <button className="chip" onClick={() => setAllergies([])}>{t.noAllergy}</button>
        </div>
      )}
    </div>
  );
}

function StepStops({ t, lang, meta, stops, setStops, stopInput, setStopInput }) {
  const sugg = meta?.stops ?? [];
  const add = (v) => {
    const s = v.trim();
    if (s && !stops.some((x) => x.toLowerCase() === s.toLowerCase())) setStops([...stops, s]);
  };
  const isOn = (name) => stops.some((x) => x.toLowerCase() === name.toLowerCase());
  const toggleName = (name) =>
    isOn(name) ? setStops(stops.filter((x) => x.toLowerCase() !== name.toLowerCase())) : add(name);
  const suggNames = sugg.map((s) => (lang === "ru" ? s.ru : s.sr).toLowerCase());
  const customs = stops.filter((s) => !suggNames.includes(s.toLowerCase()));
  return (
    <div>
      <div className="grid3">
        {sugg.map((s) => {
          const name = lang === "ru" ? s.ru : s.sr;
          const on = isOn(name);
          return (
            <button key={name} className={`tile ${on ? "stopped" : ""}`} onClick={() => toggleName(name)}>
              {on && <span className="ban"><Icon name="ban" size={13} stroke={2.4} /></span>}
              <span className="ticon"><Icon name={s.icon ?? "plant"} size={26} /></span>
              <span className="t" style={{ fontSize: 13 }}>{name}</span>
            </button>
          );
        })}
        {customs.map((s) => (
          <button key={s} className="tile stopped" onClick={() => setStops(stops.filter((x) => x !== s))}>
            <span className="ban"><Icon name="ban" size={13} stroke={2.4} /></span>
            <span className="ticon"><Icon name="salt" size={26} /></span>
            <span className="t" style={{ fontSize: 13 }}>{s}</span>
          </button>
        ))}
      </div>
      <div className="often-label">{t.ownProduct}</div>
      <div className="addrow">
        <input value={stopInput} placeholder={t.stopPlaceholder}
          onChange={(e) => setStopInput(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter") { add(stopInput); setStopInput(""); } }} />
        <button aria-label="+" onClick={() => { add(stopInput); setStopInput(""); }}>
          <Icon name="plus" size={20} />
        </button>
      </div>
    </div>
  );
}

function StepEquip({ lang, meta, equipment, setEquipment }) {
  const list = meta?.equipment ?? [];
  const toggle = (id) => setEquipment(equipment.includes(id) ? equipment.filter((x) => x !== id) : [...equipment, id]);
  return (
    <div className="grid3">
      {list.map((e) => (
        <button key={e.id} className={`tile ${equipment.includes(e.id) ? "on" : ""}`} onClick={() => toggle(e.id)}>
          {equipment.includes(e.id) && <span className="check"><Icon name="check" size={12} stroke={3} /></span>}
          <span className="ticon"><Icon name={e.id} size={26} /></span>
          <span className="t" style={{ fontSize: 13 }}>{lang === "ru" ? e.ru : e.sr}</span>
        </button>
      ))}
    </div>
  );
}

/* ---------------- Building ---------------- */
function Building({ t }) {
  const [phase, setPhase] = useState(0);
  useEffect(() => {
    const timers = [1, 2, 3, 4].map((i) => setTimeout(() => setPhase(i), i * 620));
    return () => timers.forEach(clearTimeout);
  }, []);
  const rows = [t.b1, t.b2, t.b3, t.b4];
  return (
    <main className="building">
      <div className="build-icon"><Icon name="salad" size={40} /></div>
      <h2>{t.building}</h2>
      <p className="sub">{t.buildSub}</p>
      <div className="checklist">
        {rows.map((r, i) => (
          <div key={i} className={`checkrow ${phase > i ? "done" : phase === i ? "active" : ""}`}>
            <span className="ring">{phase > i ? <Icon name="check" size={12} stroke={3} /> : ""}</span>
            <span className="t">{r}</span>
          </div>
        ))}
      </div>
    </main>
  );
}

/* ---------------- Plan ---------------- */
const PHOTOS = new Set(["chicken", "patty", "wrap", "rice", "pasta", "casserole", "stew", "soup", "pie", "fish", "salad", "porridge", "cup", "pancakes", "egg", "sandwich"]);
const dishPhoto = (icon) => `/img/${PHOTOS.has(icon) ? icon : "stew"}.jpg`;
const photoFor = (meals) => {
  const m = meals.dinner ?? meals.lunch ?? meals.breakfast;
  return dishPhoto(m?.icon);
};

function PlanView({ t, plan, storeName, onDay, onShop, onNew, onShare }) {
  const over = plan.total > plan.params.budget;
  const frac = Math.min(1, plan.total / plan.params.budget);
  const shownTotal = useCountUp(plan.total, 900, true);
  const [drawn, setDrawn] = useState(false);
  useEffect(() => { const id = requestAnimationFrame(() => setDrawn(true)); return () => cancelAnimationFrame(id); }, []);
  return (
    <main>
      {!over && <Confetti />}
      <div className="hero-plan">
        <div className="kicker">{over ? t.heroOver : t.heroDone}</div>
        <div className="bigsum">{fmt(shownTotal)}<small>{t.cur}</small></div>
        <div className="herosub">
          {over ? t.overSub : `${t.budgetLine(fmt(plan.params.budget), fmt(plan.params.budget - plan.total))}`}
        </div>
        <div className="heroBar"><i style={{ width: drawn ? `${frac * 100}%` : "0%", background: over ? "var(--amber)" : "var(--acc)" }} /></div>
      </div>
      <div className="statrow">
        <div className="stat"><b>{fmt(plan.kcal_day)}</b><span>{t.statKcal}</span></div>
        <div className="stat"><b>{fmt(plan.total / Math.max(1, plan.params.people))}</b><span>{t.statPerHead}</span></div>
        <div className="stat"><b>{DAY_IDS.reduce((s, d) => s + Object.keys(plan.days[d].meals).length, 0)}</b><span>{t.statDishes}</span></div>
      </div>
      <button className="listbtn" onClick={onShop}>
        <span>
          <span className="n">{t.positions(plan.positions)}</span>
          {t.openList}
        </span>
        <Icon name="right" size={20} />
      </button>
      <div className="seclabel">{t.secDays}</div>
      <div className="daylist">
        {DAY_IDS.map((d, i) => {
          const day = plan.days[d];
          const lang2 = document.documentElement.lang;
          const dinner = day.meals.dinner ?? day.meals.lunch ?? day.meals.breakfast;
          const dishName = dinner ? (lang2 === "ru" ? dinner.ru : dinner.sr) : "";
          if (i < 2) {
            return (
              <button className="bigday" key={d} onClick={() => onDay(i)}
                style={{ backgroundImage: `url(${photoFor(day.meals)})` }}>
                <span className="scrim" />
                <span className="ov">
                  <span className="row1">
                    <span className="dl">{t.days[i].toUpperCase()} · {t.dinner.toUpperCase()}</span>
                    <span className="pr">{fmt(day.cost)} {t.cur}</span>
                  </span>
                  <span className="dish">{dishName}</span>
                </span>
              </button>
            );
          }
          return (
            <button className="daycard" key={d} onClick={() => onDay(i)}>
              <span className="thumb" style={{ backgroundImage: `url(${photoFor(day.meals)})` }} />
              <span className="mid">
                <span className="dl">{t.daysShort[i].toUpperCase()}</span>
                <span className="dn" style={{ display: "block" }}>{dishName}</span>
              </span>
              <span className="pr">{fmt(day.cost)} {t.cur}</span>
            </button>
          );
        })}
      </div>
      <div className="plan-foot">
        <button className="cta secondary" onClick={onNew}>{t.newPlan}</button>
        <button className="cta" onClick={onShare}>{t.share}</button>
      </div>
    </main>
  );
}

/* ---------------- Day ---------------- */
function DayView({ t, lang, plan, dayIdx, setDayIdx, onBack, onSwap, onOpen }) {
  const d = DAY_IDS[dayIdx];
  const day = plan.days[d];
  const [spinning, setSpinning] = useState("");
  const touch = useRef(null);
  const groups = { breakfast: t.breakfast, lunch: t.lunch, dinner: t.dinner };
  const onTouchStart = (e) => { touch.current = { x: e.touches[0].clientX, y: e.touches[0].clientY }; };
  const onTouchEnd = (e) => {
    if (!touch.current) return;
    const dx = e.changedTouches[0].clientX - touch.current.x;
    const dy = e.changedTouches[0].clientY - touch.current.y;
    touch.current = null;
    if (Math.abs(dx) > 56 && Math.abs(dx) > Math.abs(dy) * 1.5) {
      if (dx < 0 && dayIdx < 6) setDayIdx(dayIdx + 1);
      if (dx > 0 && dayIdx > 0) setDayIdx(dayIdx - 1);
    }
  };
  return (
    <main onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
      <div className="stephead">
        <button className="backbtn" onClick={onBack}>‹ {t.back}</button>
        <span className="label">{fmt(day.cost)} {t.cur}</span>
      </div>
      <h2 style={{ fontSize: 24, fontWeight: 700, marginTop: 10 }}>{t.days[dayIdx]}</h2>
      <div className="daynav">
        {t.daysShort.map((s, i) => (
          <button key={s} className={i === dayIdx ? "on" : ""} onClick={() => setDayIdx(i)}>{s}</button>
        ))}
      </div>
      <div className="daywrap" key={d}>
      <div className="daytotal">
        <span className="l">{t.dayWhole}</span>
        <span className="r">
          <span className="pricechip">{fmt(day.cost)} {t.cur}</span>
          <span>{t.perPortion(fmt(day.cost / Math.max(1, plan.params.people)))}</span>
        </span>
      </div>
      {MEAL_ORDER.map((m) => {
        const meal = day.meals[m];
        if (!meal) return null;
        return (
          <section className="mealgroup" key={m}>
            <div className="glabel">
              <Icon name={MEAL_ICON[m]} size={15} />
              <span>{groups[m]} · {meal.family ? t.forFamily : t.forYou}</span>
            </div>
            <div className="mealcard" role="button" tabIndex={0}
              onClick={() => onOpen(meal.id, meal.servings)}
              onKeyDown={(e) => { if (e.key === "Enter") onOpen(meal.id, meal.servings); }}>
              <span className="mi photo" style={{ backgroundImage: `url(${dishPhoto(meal.icon)})` }} />
              <span className="mid">
                <span className="mn" style={{ display: "block" }}>{lang === "ru" ? meal.ru : meal.sr}</span>
                <span className="meta">
                  <span><Icon name="clock" size={13} /> {meal.time} {t.min}</span>
                  <span><Icon name="people" size={13} /> {meal.servings}</span>
                  <span><Icon name="fire" size={13} /> {fmt(meal.kcal)} kcal</span>
                </span>
              </span>
              <span className="right">
                <span className="pricechip">{fmt(meal.cost)} {t.cur}</span>
                <button className={`swapbtn ${spinning === m ? "spin" : ""}`} aria-label={t.swap}
                  onClick={(e) => { e.stopPropagation(); setSpinning(m); setTimeout(() => setSpinning(""), 500); onSwap(d, m); }}>
                  <Icon name="swap" size={15} />
                </button>
              </span>
            </div>
          </section>
        );
      })}
      </div>
    </main>
  );
}

/* ---------------- Recipe sheet ---------------- */
function CookMode({ t, name, steps, onClose }) {
  const [i, setI] = useState(0);
  const done = i >= steps.length;
  return (
    <div className="cook">
      <div className="cook-head">
        <span className="cn">{name}</span>
        <button className="iconbtn" onClick={onClose} aria-label={t.close}><Icon name="x" size={18} /></button>
      </div>
      <div className="cook-progress">
        {steps.map((_, k) => <i key={k} className={k < i || done ? "on" : ""} />)}
      </div>
      {done ? (
        <div className="cook-body">
          <div className="bigstep fin"><Icon name="check" size={46} stroke={2.5} /></div>
          <div className="cook-text" style={{ textAlign: "center" }}>
            <b style={{ display: "block", fontSize: 22, marginBottom: 8 }}>{t.bon}</b>
            {t.bonSub}
          </div>
        </div>
      ) : (
        <div className="cook-body" key={i}>
          <div className="bigstep">{i + 1}</div>
          <div className="cook-label">{t.stepShort(i + 1, steps.length)}</div>
          <div className="cook-text">{steps[i]}</div>
        </div>
      )}
      <div className="cook-foot">
        {!done && i > 0 && <button className="cta secondary" onClick={() => setI(i - 1)}>‹ {t.back}</button>}
        {done ? (
          <button className="cta" onClick={onClose}>{t.finish}</button>
        ) : (
          <button className="cta" onClick={() => setI(i + 1)}>{t.next} ›</button>
        )}
      </div>
    </div>
  );
}

function RecipeSheet({ t, lang, recipe, onClose }) {
  const { data, servings } = recipe;
  const [cooking, setCooking] = useState(false);
  const touch = useRef(null);
  const onTouchStart = (e) => { touch.current = e.touches[0].clientY; };
  const onTouchEnd = (e) => {
    if (touch.current !== null && e.changedTouches[0].clientY - touch.current > 64) onClose();
    touch.current = null;
  };
  const name = lang === "ru" ? data.ru : data.sr;
  const content = data.steps?.[lang] ?? {};
  const steps = content.steps ?? [];
  if (cooking) return <CookMode t={t} name={name} steps={steps} onClose={() => setCooking(false)} />;
  const qty = (ing) => {
    const total = ing.qty * servings;
    if (ing.unit === "pcs") return `${Math.max(1, Math.round(total))} ${t.pcs}`;
    return `${Math.round(total)} ${ing.unit === "ml" ? t.ml : t.g}`;
  };
  return (
    <div className="sheet-wrap" onClick={onClose}>
      <div className="sheet" onClick={(e) => e.stopPropagation()} role="dialog" aria-label={name}>
        <div className="sheet-photo full" style={{ backgroundImage: `url(${dishPhoto(data.icon)})` }}
          onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
          <span className="sheet-grab" />
          <button className="iconbtn close" onClick={onClose} aria-label={t.close}><Icon name="x" size={18} /></button>
          <div className="photo-ov">
            <h3>{name}</h3>
            <div className="meta">
              <span><Icon name="clock" size={13} /> {data.time} {t.min}</span>
              <span><Icon name="people" size={13} /> {servings}</span>
              <span><Icon name="fire" size={13} /> {fmt(data.kcal)} kcal</span>
            </div>
          </div>
        </div>
        <div className="sheet-body">
          <button className="cta cookbtn" onClick={() => setCooking(true)}>{t.cook}</button>
          {content.desc && <p className="sheet-desc">{content.desc}</p>}
          <div className="sheet-label">{t.ingredients}</div>
          <ul className="ing-list">
            {data.ingredients.map((ing) => (
              <li key={ing.id}>
                <span>{lang === "ru" ? ing.ru : ing.sr}</span>
                <span className="q">{qty(ing)}</span>
              </li>
            ))}
          </ul>
          <div className="sheet-label">{t.steps}</div>
          <ol className="step-list">
            {steps.map((s, i) => <li key={i}>{s}</li>)}
          </ol>
          {content.tip && (
            <div className="sheet-tip">
              <span className="tl">{t.tip}</span>
              <span>{content.tip}</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ---------------- Shopping ---------------- */
function ShopView({ t, lang, plan, checked, setChecked, onBack }) {
  const items = plan.shopping;
  const done = items.filter((i) => checked[i.id]).length;
  const cartSum = items.filter((i) => checked[i.id]).reduce((s, i) => s + i.cost, 0);
  const cats = ["meat", "dairy", "veg", "grocery", "other"];
  const byCat = (c) => items.filter((i) => i.cat === c);
  const toggle = (id) => setChecked({ ...checked, [id]: !checked[id] });
  const allDone = items.length > 0 && done === items.length;
  return (
    <main>
      {allDone && <Confetti />}
      <div className="stephead">
        <button className="backbtn" onClick={onBack}>‹ {t.back}</button>
        <span className="label">{fmt(plan.total)} {t.cur}</span>
      </div>
      <h2 style={{ fontSize: 24, fontWeight: 700, marginTop: 10 }}>{t.shopTitle}</h2>
      <div className={`shop-progress sticky ${allDone ? "alldone" : ""}`}>
        <div className="row">
          <span className="big">{allDone ? t.allDone : t.bought(done, items.length)}</span>
          {!allDone && <span className="sub">{t.keepGoing}</span>}
        </div>
        <div className="bar"><i style={{ width: `${(done / Math.max(1, items.length)) * 100}%` }} /></div>
        <div className="cart">{t.inCart(fmt(cartSum))}</div>
      </div>
      {cats.map((c) => {
        const list = byCat(c);
        if (!list.length) return null;
        const cdone = list.filter((i) => checked[i.id]).length;
        return (
          <section className="shopcat" key={c}>
            <div className="clabel">
              <span className="cl"><Icon name={`cat-${c}`} size={15} /> {t[CAT_KEY[c]]}</span>
              <span>{cdone}/{list.length}</span>
            </div>
            <div className="shopitems">
              {list.map((i) => (
                <button key={i.id} className={`shopitem ${checked[i.id] ? "done" : ""}`} onClick={() => toggle(i.id)}>
                  <span className="box">{checked[i.id] ? <Icon name="check" size={13} stroke={3} /> : ""}</span>
                  <span className="mid">
                    <span className="n" style={{ display: "block" }}>{lang === "ru" ? i.ru : i.sr}</span>
                    <span className="q" style={{ display: "block" }}>
                      {i.packs > 1 ? `${i.packs} × ` : ""}{lang === "ru" ? i.lab_ru : i.lab_sr}
                    </span>
                  </span>
                  <span className="p">{fmt(i.cost)} {t.cur}</span>
                </button>
              ))}
            </div>
          </section>
        );
      })}
    </main>
  );
}
