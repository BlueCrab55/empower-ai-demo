
import streamlit as st
from utils import init_state

st.set_page_config(page_title="AI Clinical Reasoning — Garmin/Whoop Demo", page_icon="🧭", layout="wide")
init_state()

st.markdown("<h1 style='margin-top:0'>AI Clinical Reasoning — Garmin/Whoop-Style Demo</h1>", unsafe_allow_html=True)
st.write("Use the sidebar to navigate: Dashboard, Intake, Session, Gateway Tests, Insights.")
st.markdown("— Built from your OS + Logic Engine + Exercise Library specs —")
