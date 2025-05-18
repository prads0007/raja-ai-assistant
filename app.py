import streamlit as st

st.set_page_config(page_title="RAJA AI Assistant", layout="wide")
st.title("RAJA AI Assistant")

# Sidebar with only Stock Screener for now (you can add more later)
selected_module = st.sidebar.selectbox("Choose Module", ["Stock Screener"])

if selected_module == "Stock Screener":
    import stock_screener  # This runs the code in stock_screener.py
