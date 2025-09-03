
import streamlit as st
from utils import init_state, divider

init_state()
st.markdown("## Longitudinal Insights")
st.write("Monthly correlations & trends mined from readiness + performance + subjective data.")

st.info("Insight: Days after sleep ≤2/5, your deep squat RPE is +1.2 at same load. Let’s front‑load lighter positional work after poor sleep and push heavier on good‑sleep days.")

st.markdown("### Trend Cards")
c1,c2 = st.columns(2)
with c1:
    st.write("**Knee-to-Wall (cm)** — baseline 7–8 → target 9+")
    st.progress(0.7)
with c2:
    st.write("**Deep Squat Hold (s)** — baseline 45 → target 90")
    st.progress(0.5)

st.markdown("### Exports")
st.download_button("Download Demo Plan JSON", data='{"demo":"plan"}', file_name="demo_plan.json")
