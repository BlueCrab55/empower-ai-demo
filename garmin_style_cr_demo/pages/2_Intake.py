
import streamlit as st
from utils import init_state, divider

init_state()
st.markdown("## Intake & Safety")

st.write("**Echo & Lead:** ‘Got your goal of deep squat comfort + horse stance/pancake. Quick safety check to keep us smart.’")

in_pain = st.radio("Are you in any pain right now?", ["Yes","No"], index=0, horizontal=True)
loc = st.selectbox("Primary location", ["Hip","Knee","Ankle","Low Back","Neck/Head"])

if loc in ["Neck/Head","Low Back"]:
    st.subheader("Spinal & Neurological Safety Screen")
    s1 = st.checkbox("Major trauma?")
    s2 = st.checkbox("Unexplained weight loss/fever/chills?")
    s3 = st.checkbox("Bowel/bladder changes or saddle numbness?")
    s4 = st.checkbox("Dizziness/double vision/swallow/speech issues/fainting?")
    red = any([s1,s2,s3,s4])
else:
    st.subheader("Peripheral Joint Safety Screen")
    p1 = st.checkbox("Significant swelling/deformity or unable to bear weight?")
    p2 = st.checkbox("Area hot/red with fever?")
    red = any([p1,p2])

if red:
    st.error("Red flag present — safest next step is in-person medical evaluation. Intake halts here.")
else:
    st.success("Safety screen passed.")

divider()
st.markdown("### Primary Triage")
triage = st.radio("What best describes your primary goal?", [
    "Pain/discomfort",
    "Performance",
    "Both (performance with discomfort)",
    "Flexibility/Mobility",
    "Longevity/Prevention"
], index=3)

st.markdown("### Coaching Persona")
persona = st.selectbox("Pick a style", ["The Nurturer","The Analyst","The Motivator","The Minimalist"], index=1)
st.session_state["profile"]["persona"] = persona

divider()
st.markdown("### Practical Constraints")
d = st.number_input("Days per week you can commit", 1, 7, value=4)
t = st.number_input("Session length (minutes)", 20, 120, value=60)
equip = st.text_input("Equipment", value=st.session_state["profile"]["equipment"])
st.session_state["profile"]["days_per_week"] = int(d)
st.session_state["profile"]["session_length_min"] = int(t)
st.session_state["profile"]["equipment"] = equip

divider()
st.markdown("### AMS Screen (Goal-tailored)")
st.write("**We’ll test:** Knee-to-Wall Dorsiflexion, Deep Squat Hold (30–60s), 90/90 ER-IR Control, Single-Leg Balance.")
k2w_R = st.slider("Knee-to-Wall (cm) — Right", 0, 20, 8)
k2w_L = st.slider("Knee-to-Wall (cm) — Left", 0, 20, 7)
ds = st.slider("Deep Squat Hold (seconds)", 0, 180, 45)
sl_R = st.slider("Single-Leg Balance (sec) — Right", 0, 120, 20)
sl_L = st.slider("Single-Leg Balance (sec) — Left", 0, 120, 20)

st.session_state["assessments"] = {
    "knee_to_wall_cm": {"R": k2w_R, "L": k2w_L},
    "deep_squat_hold_s": ds,
    "hip_9090_control": "moderate tremor",
    "sl_balance_s": {"R": sl_R, "L": sl_L}
}

st.success("Stored baselines. ‘We’ll use these to tailor your plan and track progress.’")
