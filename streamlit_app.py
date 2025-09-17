# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global Balance Dashboard", layout="wide")

# -----------------------------
# Styling: Pink background, Orange + White accents
# -----------------------------
st.markdown("""
<style>
    /* --- App background --- */
    .stApp {
        background-color: #ff414e;  /* Pink/Red background */
        color: #ffffff;             /* White text */
    }

    /* --- Top header style --- */
    .header {
        background-color: #ff8928;  /* Orange bar */
        padding: 14px 28px;
        border-bottom: 2px solid #ffffff;
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #ffffff;  /* White text */
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;  /* White sidebar */
        color: #000000;
        padding-top: 28px;
    }

    /* --- Navigation buttons --- */
    div[role="radiogroup"] label {
        display: block;
        background: #ff414e;          /* Pink */
        color: #ffffff !important;
        padding: 12px 16px;
        border-radius: 10px;
        margin: 8px 16px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        border: 1px solid #ff8928;    /* Orange border */
        text-align: center;
        width: 85% !important;
    }
    div[role="radiogroup"] label:hover {
        background: #ff8928;          /* Orange hover */
        color: #ffffff !important;
        transform: translateY(-2px);
    }
    div[role="radiogroup"] label[aria-checked="true"] {
        background: #ffffff !important;   /* Active = white */
        color: #ff414e !important;        /* Pink text */
        border: 2px solid #ff8928;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* --- Primary buttons --- */
    div.stButton > button {
        background-color: #ffffff;   /* White button */
        color: #ff414e;              /* Pink text */
        border-radius: 8px;
        padding: 12px 20px;
        font-weight: 600;
        border: 2px solid #ff8928;
        transition: background-color 0.2s, transform 0.2s;
        display: block;
        margin: 12px auto;
        width: 240px;
    }
    div.stButton > button:hover {
        background-color: #ff8928;   /* Orange hover */
        color: #ffffff;
        transform: translateY(-2px);
    }

    /* --- Inputs --- */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 1px solid #ffffff !important;
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* --- Headings --- */
    h1, h2, h3 {
        color: #ffffff;  /* White headings */
    }

    /* --- Card --- */
    .iframe-card {
        background: #ffffff;
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
  <h1>🌍 &nbsp; Global Balance</h1>
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
    st.markdown("""
    ### 📌 Key Observations:
    - Countries with **higher Gini Index** show **greater inequality**.  
    - Developed nations often have **lower inequality** but slower improvement.  
    - Developing countries display **wider income gaps** due to uneven distribution.  
    - Population growth in some regions correlates with **higher inequality trends**.  
    - Wealth concentration is highest in the **top 10%**, especially in emerging markets.  

    ---
    ✅ These insights help policymakers and researchers design **targeted solutions**.
    """)

elif page == "About":
    st.markdown("## ℹ️ About This Project")
    st.markdown("""
    ### 🌍 Global Balance – Income Inequality Dashboard  

    This project is designed to **analyze and visualize global income inequality**.  
    It combines interactive dashboards with powerful analytics to highlight inequality patterns.  

    #### 🎯 Objectives:
    - Measure **income inequality using Gini Index**.  
    - Compare **top 10% vs bottom 10% income share**.  
    - Track **global and country-level changes (2000–2023)**.  
    - Provide actionable insights for **researchers, students, and policymakers**.  

    #### 🛠️ Tools Used:
    - **Power BI** → For interactive dashboard visuals.  
    - **Streamlit & Python (Pandas)** → For web app integration.  

    ---
    ✅ *Making inequality data more **transparent, interactive, and actionable.***
    """)

elif page == "Feedback":
    st.markdown("## 📝 Feedback")

    # --- Fix: Form with star rating ---
    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("Your feedback")

        st.markdown("### ⭐ Rate this Dashboard")
        # Star rating buttons
        cols = st.columns(5)
        rating = 0
        for i, col in enumerate(cols, start=1):
            if col.button("⭐ " * i, key=f"star_{i}"):
                rating = i

        submitted = st.form_submit_button("Send Feedback")

        if submitted:
            if feedback.strip() and rating > 0:
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
                st.success(f"✅ Thank you! Feedback saved with rating {rating} ⭐")
            else:
                st.error("⚠️ Please enter feedback and select a rating.")

    # --- Show previous feedback ---
    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
