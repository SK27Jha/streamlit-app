# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global income inequality dashboard", layout="wide")

# -----------------------------
# Styling (Light Green + Light Blue Nav + Pink/Orange Highlights)
# -----------------------------
st.markdown("""
<style>
    /* --- App background --- */
    .stApp {
        background-color: #90ee90;  /* Light Green Background */
        color: #12343b;
    }

    /* --- Top header style --- */
    .header {
        background-color: #ff414e;  /* Pink/Red */
        padding: 14px 28px;
        border-bottom: 2px solid #ff8928;
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #ffffff;  /* White */
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: #ff414e;  /* Pink/Red */
        color: #ffffff;
        padding-top: 28px;
    }

    /* --- Navigation buttons (Light Blue style) --- */
    div[role="radiogroup"] label {
        display: block;
        background: #add8e6;        /* Light Blue */
        color: #12343b !important;
        padding: 12px 16px;
        border-radius: 10px;
        margin: 8px 16px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        border: 1px solid #87ceeb;
        text-align: center;
        width: 85% !important;
    }
    div[role="radiogroup"] label:hover {
        background: #87ceeb;        /* Sky Blue hover */
        color: #ffffff !important;
        transform: translateY(-2px);
    }
    div[role="radiogroup"] label[aria-checked="true"] {
        background: #4682b4 !important;   /* Steel Blue when active */
        color: #ffffff !important;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* --- Primary buttons --- */
    div.stButton > button {
        background-color: #ff414e;
        color: #ffffff;
        border-radius: 8px;
        padding: 12px 20px;
        font-weight: 600;
        border: none;
        transition: background-color 0.2s, transform 0.2s;
        display: block;
        margin: 12px auto;
        width: 240px;
    }
    div.stButton > button:hover {
        background-color: #ff8928;
        transform: translateY(-2px);
    }

    /* --- Inputs --- */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 1px solid #ff414e !important;
    }

    /* --- Headings --- */
    h1, h2, h3 {
        color: #ff414e;
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
  <h1>🌍 &nbsp;Global Income Inequality Dashboard</h1>
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

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("Your feedback")
        rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)

        submitted = st.form_submit_button("Send Feedback")

        if submitted:
            if feedback.strip():
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
                st.success(f"✅ Thank you! Feedback saved with rating {rating}/5")
            else:
                st.error("⚠️ Please enter feedback before submitting.")

    # --- Show previous feedback ---
    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
