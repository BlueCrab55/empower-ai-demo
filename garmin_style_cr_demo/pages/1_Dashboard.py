
import streamlit as st
from utils import init_state, readiness_band, progress_bar, divider, tag_chip

init_state()
p = st.session_state["profile"]
prog = st.session_state["progress"]
today = st.session_state["today_readiness"]
pain = st.session_state["today_pain_10"]
adherence = st.session_state["adherence_week"]
phase = st.session_state["phase"]

st.markdown("## Dashboard")

c1,c2,c3,c4 = st.columns(4)
with c1:
    st.metric("Primary Goal", "Hip/Squat Mobility")
with c2:
    st.metric("Readiness Today", f"{today}/100", delta=None)
with c3:
    st.metric("Pain (now)", f"{pain}/10")
with c4:
    st.metric("Adherence (week)", f"{int(adherence*100)}%")

band, action = readiness_band(today)
st.info(f"**Readiness: {band}** — {action}")

st.markdown("### Goal Progress")
c1,c2 = st.columns(2)
with c1:
    progress_bar("Goal Path — Squat Mobility", prog["goal_path"])
    progress_bar("Pancake End-Range Strength", prog["pancake_strength"])
with c2:
    progress_bar("Skill Tree — Hip Mobility", prog["skill_tree"])
    progress_bar("Weekly Volume (lower)", prog["weekly_volume_lower"])

divider()

st.markdown("### Current Phase & Quick Actions")
st.success(f"**Phase {phase}** — Positional Awareness & Unloaded Isometrics (Weeks 1–3)")
c1,c2,c3,c4 = st.columns(4)
with c1: st.button("▶️ Start Session", use_container_width=True)
with c2: st.button("🔧 Adjust Plan", use_container_width=True)
with c3: st.button("💬 AI Chat", use_container_width=True)
with c4: st.button("📝 Log Pain", use_container_width=True)

divider()

st.markdown("### This Week")
st.write("- Mon — Mobility + Upper Body")
st.write("- Tue — M3 Intensive (Hip focus)")
st.write("- Thu — Run (4×4)")
st.write("- Fri — M3 Intensive (Hip focus)")
st.write("- Sat — Zone-2 Run")

st.caption("Echo & Lead + Contextual Response are used in all interactions.")
