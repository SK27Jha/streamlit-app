# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global Balance Dashboard", layout="wide")

# -----------------------------
# Styling: Night Blue + Sand Tan
# -----------------------------
st.markdown("""
<style>
    /* --- App background (Night Blue) --- */
    .stApp {
        background-color: #2d545e;  /* Night Blue */
        color: #FFFFFF;  /* White text for contrast */
    }

    /* --- Top header style --- */
    .header {
        background-color: #12343b;  /* Night Blue Shadow */
        padding: 14px 28px;
        border-bottom: 2px solid #c89666; /* Sand Tan Shadow */
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #e1b382;  /* Sand Tan */
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: #12343b;  /* Night Blue Shadow */
        color: #FFFFFF;
        padding-top: 28px;
    }

    /* --- Navigation buttons --- */
    div[role="radiogroup"] label {
        display: block;
        background: #e1b382;          /* Sand Tan */
        color: #12343b !important;    /* Night Blue Shadow text */
        padding: 12px 16px;
        border-radius: 10px;
        margin: 8px 16px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        border: 1px solid #c89666;   /* Sand Tan Shadow */
        text-align: center;
        width: 85% !important;       /* Equal width */
    }
    div[role="radiogroup"] label:hover {
        background: #c89666;          /* Sand Tan Shadow */
        color: #FFFFFF !important;
        transform: translateY(-2px);
    }
    div[role="radiogroup"] label[aria-checked="true"] {
        background: #12343b !important;   /* Night Blue Shadow active */
        color: #e1b382 !important;        /* Sand Tan text */
        border: 2px solid #e1b382;        /* Sand Tan border */
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    /* --- Primary buttons --- */
    div.stButton > button {
        background-color: #e1b382;   /* Sand Tan */
        color: #12343b;              /* Night Blue Shadow text */
        border-radius: 8px;
        padding: 12px 20px;
        font-weight: 600;
        border: none;
        transition: background-color 0.2s, transform 0.2s;
        display: block;
        margin: 12px auto;   /* Center buttons */
        width: 240px;
    }
    div.stButton > button:hover {
        background-color: #c89666;   /* Sand Tan Shadow */
        color: #FFFFFF;
        transform: translateY(-2px);
    }

    /* --- Inputs --- */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 1px solid #e1b382 !important;
        background-color: #ffffff !important;
        color: #12343b !important;
    }

    /* --- Headings --- */
    h1, h2, h3 {
        color: #e1b382;  /* Sand Tan */
    }

    /* --- Card --- */
    .iframe-card {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
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

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("Your feedback")
        rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, step=1)
        submitted = st.form_submit_button("Send Feedback")

        if submitted:
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
