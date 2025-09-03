
import json, os, math, time
import pandas as pd
import numpy as np
import streamlit as st

STATE_KEYS_DEFAULTS = {
    "profile": {
        "primary_goal": "Sit comfortably in a deep squat; progress to horse stance & pancake",
        "why": "Move freely, demo to patients, enjoy training",
        "secondary_goals": ["Upper-body maintenance", "VO2 & leanness"],
        "days_per_week": 4,
        "session_length_min": 60,
        "equipment": "Garage gym (barbell, rack, DBs, bands)",
        "training_status": "Intermediate"
    },
    "assessments": {
        "knee_to_wall_cm": {"R": 8, "L": 7},
        "deep_squat_hold_s": 45,
        "hip_9090_control": "moderate tremor",
        "sl_balance_s": {"R": 20, "L": 20}
    },
    "readiness_history": [],
    "today_readiness": 82,
    "today_pain_10": 2,
    "adherence_week": 0.40,
    "phase": 1,
    "progress": {
        "goal_path": 0.65,
        "skill_tree": 0.5,
        "pancake_strength": 0.30,
        "weekly_volume_lower": 0.75
    },
    "ams_targets": [
        {"name":"Knee-to-Wall Dorsiflexion","tag":"Assess-Dorsiflexion","baseline":"7–8 cm"},
        {"name":"Deep Squat Hold","tag":"Assess-Functional-Squat","baseline":"45 s"},
        {"name":"90/90 ER-IR Control","tag":"Assess-End-Range-Control","baseline":"moderate tremor"}
    ],
    "library_has_assess_tags": True
}

def init_state():
    for k,v in STATE_KEYS_DEFAULTS.items():
        if k not in st.session_state:
            st.session_state[k] = v

def readiness_band(score:int):
    if score >= 85: return "Green", "Proceed as planned."
    if score >= 60: return "Yellow", "Reduce volume by ~15–20%, keep intensity."
    return "Red", "Replace with recovery mobility + easy cardio."

def progress_bar(label, frac:float):
    st.write(f"**{label}**")
    st.progress(min(max(frac,0),1.0))

def tag_chip(text):
    st.markdown(f"<span style='padding:4px 8px;border-radius:12px;background:#111;border:1px solid #333;font-size:12px'>{text}</span>", unsafe_allow_html=True)

def divider():
    st.markdown("<hr style='border:1px solid #222'/>", unsafe_allow_html=True)

def two_dp(x):
    try: return round(float(x),2)
    except: return x

# ---- Extended Brand (glass + neon) ----
BRAND.update({
    "gradient_bg": "linear-gradient(135deg, #0A0C12 0%, #0F1424 40%, #101a2e 100%)",
    "glass_bg": "rgba(255,255,255,0.05)",
    "glass_border": "rgba(255,255,255,0.12)",
    "neon": "#7DF9FF",
    "text": "#E6EEF3",
    "muted": "#9FB3C8"
})

def inject_glass_css():
    st.markdown(f'''
    <style>
      .stApp {{
        background: {BRAND["gradient_bg"]};
        color: {BRAND["text"]};
      }}
      .glass {{
        background: {BRAND["glass_bg"]};
        border: 1px solid {BRAND["glass_border"]};
        border-radius: 18px;
        padding: 18px 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
      }}
      .title-accent {{
        font-weight: 700;
        letter-spacing: .2px;
      }}
      .chip {{
        display:inline-block;
        padding:6px 10px;
        border-radius:12px;
        border:1px solid {BRAND["glass_border"]};
        background:{BRAND["glass_bg"]};
        color:{BRAND["muted"]};
        font-size:12px;
        margin-right:6px;
      }}
      /* Progress ring container */
      .ring {{
        width: 130px; height: 130px; position: relative; display:inline-block;
        margin: 6px 10px;
      }}
      .ring svg {{ transform: rotate(-90deg); }}
      .ring .label {{
        position: absolute; top: 50%; left: 50%;
        transform: translate(-50%, -55%);
        text-align: center; color: {BRAND["text"]};
        font-weight: 600; font-size: 22px;
      }}
      .ring .sub {{
        position: absolute; top: 65%; left: 50%;
        transform: translate(-50%, 0);
        color: {BRAND["muted"]}; font-size: 12px;
      }}
      .neon {{
        text-shadow: 0 0 8px {BRAND["neon"]}55, 0 0 18px {BRAND["neon"]}33;
        color: {BRAND["neon"]};
      }}
      .metric-card {{
        display:flex; gap:14px; align-items:center;
      }}
    </style>
    ''', unsafe_allow_html=True)

def radial_progress(percent: float, label: str, subtitle: str = ""):
    pct = max(0.0, min(1.0, float(percent)))
    # circle math
    r = 56
    circ = 2 * 3.14159 * r
    dash = circ * pct
    gap = circ - dash
    html = f'''
    <div class="ring">
      <svg width="130" height="130">
        <circle cx="65" cy="65" r="{r}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="12"></circle>
        <circle cx="65" cy="65" r="{r}" fill="none"
                stroke="{BRAND["primary"]}" stroke-width="12"
                stroke-linecap="round"
                stroke-dasharray="{dash} {gap}"></circle>
      </svg>
      <div class="label">{int(pct*100)}</div>
      <div class="sub">{subtitle or label}</div>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
