
# PhysioAI — API Demo

## Features
- Streamlit app with chat UI
- Messages persisted in SQLite (`data/app.db`)
- Optional **API-backed chat**: set `LLM_API_KEY` (and optionally `LLM_MODEL`, `LLM_API_BASE`)

## Run
```bash
pip install -r requirements.txt
export LLM_API_KEY=sk-...
streamlit run Home.py
```
