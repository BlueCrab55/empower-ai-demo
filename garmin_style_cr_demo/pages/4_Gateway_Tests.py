
import streamlit as st
from utils import init_state, divider

init_state()
st.markdown("## Gateway Tests")
st.write("Matches `Assess-` tags in your Exercise Library; OS pauses flow, collects metrics, and unlocks next phase on pass.")

tag = st.text_input("Search Assess Tag", value="Assess-")
st.info("Examples found: Assess-Dorsiflexion, Assess-Functional-Squat, Assess-End-Range-Control")
st.success("Demo: Library has assessment tags.")

st.markdown("### Example Phase Gateways")
st.write("- Deep Squat Hold ≥60s pain ≤3/10")
st.write("- Knee-to-Wall ≥9 cm (both sides)")
st.write("- Smooth 90/90 control transitions")

st.button("Record Results & Validate", use_container_width=True)
