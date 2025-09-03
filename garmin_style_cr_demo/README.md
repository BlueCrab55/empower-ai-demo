
# Garmin/Whoop-Style Clinical Reasoning Demo

A Streamlit **multi-page** app that showcases your **AI Operating System + Logic Engine** with a Garmin/Whoop-style dashboard. Zero backend required.

## Run locally
```bash
pip install -r requirements.txt
streamlit run Home.py
```
Then open http://localhost:8501

## Deploy to Streamlit Cloud
1. Push this folder to a public GitHub repo (root must contain `Home.py`, `pages/`, `utils.py`, `requirements.txt`).
2. In Streamlit Cloud, set **Main file** to `Home.py`.
3. Deploy — it will generate a public URL you can share.

## What’s implemented
- **Dashboard** with progress bars, readiness, adherence, pain, quick actions
- **Intake & Safety** with spinal/peripheral logic, AMS baseline capture
- **Start Session** with **Readiness bands** (Green/Yellow/Red) auto‑adjust
- **Exercise Swap Protocol** (UI demo and messaging)
- **Gateway Tests** referencing `Assess-` tags
- **Insights** page with a sample correlation card + trend bars
- **Session State** emulates a user profile and baselines

> Swap in your real Exercise Library page later by adding an uploader and filtering by tags (`PrimaryGoal`, `MovementPattern`, `SpecificApplication` with `Assess-`).

## Requirements
- Python 3.10+
- Packages in `requirements.txt`
