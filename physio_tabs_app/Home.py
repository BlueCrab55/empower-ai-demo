
import streamlit as st, os, sqlite3, datetime, json, pandas as pd, requests

st.set_page_config(page_title="PhysioAI — API Demo", page_icon="🦾", layout="wide")

DB_PATH = os.path.join("data","app.db")
LLM_API_BASE = os.getenv("LLM_API_BASE","https://api.openai.com/v1")
LLM_API_KEY  = os.getenv("LLM_API_KEY","")
LLM_MODEL    = os.getenv("LLM_MODEL","gpt-4o-mini")

def init_db():
    os.makedirs("data", exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.execute("CREATE TABLE IF NOT EXISTS chat (user_id TEXT, ts TEXT, role TEXT, message TEXT)")
    con.commit(); return con

def fetch_chat(con, user_id="demo"):
    return pd.read_sql_query("SELECT * FROM chat WHERE user_id=? ORDER BY ts ASC", con, params=(user_id,))

def append_chat(con, role, msg, user_id="demo"):
    con.execute("INSERT INTO chat VALUES (?,?,?,?)",(user_id,datetime.datetime.utcnow().isoformat(),role,msg)); con.commit()

def llm_chat(messages):
    if not LLM_API_KEY: return "⚠️ No API key set. Using local stub."
    try:
        r=requests.post(f"{LLM_API_BASE}/chat/completions",
            headers={"Authorization":f"Bearer {LLM_API_KEY}","Content-Type":"application/json"},
            json={"model":LLM_MODEL,"messages":messages,"temperature":0.2},timeout=30)
        r.raise_for_status(); return r.json()["choices"][0]["message"]["content"]
    except Exception as e: return f"⚠️ API error: {e}"

con=init_db()
st.markdown("## 🤖 PhysioAI — API Chat Demo")
st.caption("Messages stored in local SQLite. Set LLM_API_KEY to enable real API replies.")

for _,row in fetch_chat(con).iterrows():
    with st.chat_message(row["role"]): st.write(row["message"])

if prompt:=st.chat_input("Ask your AI physio coach..."):
    append_chat(con,"user",prompt)
    msgs=[{"role":"system","content":"You are a concise AI physio coach. Keep replies short."}]
    for _,r in fetch_chat(con).tail(6).iterrows():
        msgs.append({"role":r["role"],"content":r["message"]})
    reply=llm_chat(msgs)
    append_chat(con,"assistant",reply)
    with st.chat_message("assistant"): st.write(reply)
