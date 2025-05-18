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
import streamlit as st
import datetime

# Title
st.set_page_config(page_title="RAJA - AI Assistant", layout="wide")
st.title("👑 RAJA - Your Personal AI Assistant")
st.subheader("🧠 Powered Daily Routine for Praduman Pandey")

# Predefined Daily Routine
daily_routine = [
    {"time": "05:30 AM", "task": "Wake up + Drink water"},
    {"time": "05:45 AM", "task": "100 Dand, 50 Sapate, 10 min Shadow Boxing"},
    {"time": "06:30 AM", "task": "Cold shower + Clean breakfast"},
    {"time": "07:00 AM", "task": "Morning Review (RAJA Summary + Planner)"},
    {"time": "08:00 AM", "task": "Forex Market Analysis + Journal"},
    {"time": "09:00 AM", "task": "Stock Screener + Fundamental Research"},
    {"time": "11:00 AM", "task": "Walk + Listen to one podcast (Finance/Mindset)"},
    {"time": "01:00 PM", "task": "Lunch (clean) + Rest (30 min)"},
    {"time": "02:00 PM", "task": "Self-Learning: Python / Finance Course"},
    {"time": "04:00 PM", "task": "Evening Walk + Light Meditation"},
    {"time": "06:00 PM", "task": "Re-analyze Trades + Market Notes"},
    {"time": "07:30 PM", "task": "Dinner (early, clean)"},
    {"time": "08:30 PM", "task": "RAJA Assistant Reflection + Journal"},
    {"time": "09:30 PM", "task": "Sleep"}
]

st.markdown("## ✅ Today's Routine")
completed_tasks = []

for item in daily_routine:
    task = st.checkbox(f"{item['time']} — {item['task']}")
    if task:
        completed_tasks.append(item['task'])

# Reflection
st.markdown("---")
st.markdown("## 📔 Daily Reflection")
mood = st.selectbox("How did you feel today?", ["😎 Great", "🙂 Good", "😐 Okay", "😟 Bad", "😞 Worst"])
notes = st.text_area("Journal Notes", placeholder="Write your thoughts, wins, struggles...")

# Summary
st.markdown("---")
st.markdown("## 📊 Summary")
st.write(f"✅ Tasks Completed: **{len(completed_tasks)} / {len(daily_routine)}**")
if len(completed_tasks) >= 10:
    st.success("Excellent discipline today, King!")
elif len(completed_tasks) >= 6:
    st.info("Good job, stay consistent.")
else:
    st.warning("Let’s do better tomorrow.")

st.write(f"🧠 Mood: {mood}")
if notes:
    st.write("📝 Your Journal Entry:")
    st.info(notes)

st.markdown("---")
st.markdown("Made with ❤️ by your loyal AI, RAJA")

