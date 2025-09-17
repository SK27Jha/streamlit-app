# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global income inequality Dashboard", layout="wide")

# -----------------------------
# Styling: Cream background + button layout
# -----------------------------
st.markdown("""
<style>
    /* --- App background --- */
    .stApp {
        background-color: #FDEBD0;  /* Cream background */
        color: #0f1724;
    }

    /* --- Top header style --- */
    .header {
        background-color: #DC143C;  /* Crimson */
        padding: 14px 28px;
        border-bottom: 2px solid #F75270;
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #FFFFFF;
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: #DC143C;  /* Crimson */
        color: #FFFFFF;
        padding-top: 28px;
    }
    section[data-testid="stSidebar"] .css-1d391kg,
    section[data-testid="stSidebar"] .css-1fv8s86 {
        color: #FFFFFF !important;
    }

    /* --- Navigation buttons --- */
    div[role="radiogroup"] label {
        display: block;
        background: #F7CAC9;          /* Soft pink default */
        color: #0f1724 !important;
        padding: 10px 14px;
        border-radius: 10px;
        margin: 6px 12px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        border: 1px solid #F75270;
        text-align: center;
    }
    div[role="radiogroup"] label:hover {
        background: #F75270;
        color: #FFFFFF !important;
        transform: translateY(-2px);
    }
    div[role="radiogroup"] label[aria-checked="true"] {
        background: #DC143C !important;
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* --- Primary buttons --- */
    div.stButton > button {
        background-color: #DC143C;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 12px 20px;
        font-weight: 600;
        border: none;
        transition: background-color 0.2s, transform 0.2s;
        display: block;
        margin: 12px auto;   /* Center buttons */
        width: 220px;        /* Fixed width for consistency */
    }
    div.stButton > button:hover {
        background-color: #F75270;
        transform: translateY(-2px);
    }

    /* --- Inputs --- */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 1px solid #DC143C !important;
    }

    /* --- Headings --- */
    h1, h2, h3 {
        color: #DC143C;
    }

    /* --- Card --- */
    .iframe-card {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Nav
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Dashboard", "Insight", "About", "Feedback"])

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="header">
  <h1>🌍 &nbsp;Global income income inequality</h1>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Pages
# -----------------------------
if page == "Login":
    st.markdown("## 🔑 Login Page")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("✅ Login Successful!")
        else:
            st.error("❌ Invalid Username or Password")

elif page == "Dashboard":
    st.markdown("## 📊 Dashboard")
    st.markdown('<div class="iframe-card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Insight":
    st.markdown("## 🔎 Insights from Dashboard")
    st.write("📌 Highlights about global income inequality, trends, and observations...")

elif page == "About":
    st.markdown("## ℹ️ About This Project")
    st.write("This dashboard helps visualize global inequality using Gini Index and income distribution.")

elif page == "Feedback":
    st.markdown("## 📝 Feedback")
    feedback = st.text_area("Your feedback")
    rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5)
    if st.button("Send Feedback"):
        if feedback:
            feedback_data = {
                "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Feedback": [feedback],
                "Rating": [rating],
            }
            df_new = pd.DataFrame(feedback_data)
            if os.path.exists("feedback.csv"):
                df_existing = pd.read_csv("feedback.csv")
                df = pd.concat([df_existing, df_new], ignore_index=True)
            else:
                df = df_new
            df.to_csv("feedback.csv", index=False)
            st.success("✅ Thank you! Feedback saved.")
        else:
            st.error("⚠️ Please enter feedback before submitting.")
    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
