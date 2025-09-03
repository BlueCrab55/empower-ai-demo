
import streamlit as st
from utils import init_state, readiness_band, divider, tag_chip

init_state()
st.markdown("## Start Session")
st.write("Daily Readiness → Action")

sleep = st.slider("Sleep Quality (1-5)", 1, 5, 4)
stress = st.slider("Life Stress (1-5) (1=high, 5=low)", 1, 5, 3)
energy = st.slider("Energy Level (1-5)", 1, 5, 4)
soreness = st.slider("Muscle Soreness (1-5) (1=very sore, 5=not sore)", 1, 5, 3)

score = round(25*(sleep/5.0)+25*((6-stress)/5.0)+25*(energy/5.0)+25*((6-soreness)/5.0),1)
st.session_state["today_readiness"] = score
band, action = readiness_band(score)
st.info(f"Readiness {score}/100 — **{band}**. {action}")

divider()
st.markdown("### Today’s Plan (Phase 1 — Positional Awareness)")
if band == "Yellow":
    st.caption("Auto-adjust: –15–20% volume (kept intensities the same).")

st.write("- 90/90 ER-IR Isometrics — 10–15s holds ×3 (pain ≤3/10)")
st.write("- Knee-to-Wall Dorsiflexion — 2–3 sets (may remove 1 set if Yellow)")
st.write("- Deep Squat Counterbalance Holds — 20–30s ×2")
st.write("- Optional: Glute Bridge Iso")

divider()
st.markdown("### Exercise Swap Protocol (Preference/Constraints)")
st.write("If an exercise doesn’t feel right:")
c1,c2 = st.columns(2)
with c1:
    st.write("**Swap options today:**")
    st.write("- 90/90 → Jefferson Curl (light)")
    st.write("- Counterbalance Hold → Goblet Pause Squat (light)")
with c2:
    st.button("Swap to Jefferson Curl", use_container_width=True)
    st.button("Swap to Goblet Pause Squat", use_container_width=True)

st.success("The OS will explain substitutions (why) to reinforce trust and transparency.")
