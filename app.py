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
