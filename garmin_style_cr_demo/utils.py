
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
