import streamlit as st
import datetime

# Task manager
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

def add_task(task):
    today = str(datetime.date.today())
    if today not in st.session_state.tasks:
        st.session_state.tasks[today] = []
    st.session_state.tasks[today].append({"task": task, "done": False})

def toggle_task_done(day, index):
    st.session_state.tasks[day][index]["done"] = not st.session_state.tasks[day][index]["done"]

# Fake stock data (for now)
def get_smallcap_stocks():
    return [
        {"symbol": "ABC", "price": 120, "pe": 15, "pb": 1.2, "roe": 18},
        {"symbol": "XYZ", "price": 55, "pe": 8, "pb": 0.9, "roe": 20},
        {"symbol": "DEF", "price": 220, "pe": 10, "pb": 1.5, "roe": 12},
    ]

# UI
st.title("🤖 RAJA - Your AI Personal Assistant")

st.header("📅 Daily Routine")
task_input = st.text_input("Add a task:")
if st.button("Add") and task_input.strip():
    add_task(task_input.strip())
    st.success(f"Task added: {task_input.strip()}")

today = str(datetime.date.today())
tasks_today = st.session_state.tasks.get(today, [])

if tasks_today:
    for i, t in enumerate(tasks_today):
        col1, col2 = st.columns([8,1])
        col1.markdown(f"- {'~~' if t['done'] else ''}{t['task']}{'~~' if t['done'] else ''}")
        if col2.button("✅" if not t["done"] else "↩️", key=f"toggle_{i}"):
            toggle_task_done(today, i)
            st.experimental_rerun()
else:
    st.info("No tasks for today.")

st.markdown("---")
st.header("📈 Stock Screener (Demo)")
stocks = get_smallcap_stocks()
filtered = [s for s in stocks if s["pe"] < 15 and s["pb"] < 1.5 and s["roe"] > 12]

if filtered:
    for s in filtered:
        st.markdown(f"**{s['symbol']}** — ₹{s['price']} | P/E: {s['pe']} | P/B: {s['pb']} | ROE: {s['roe']}%")
else:
    st.info("No matching stocks found.")

st.caption("🧠 More features coming soon...")
