# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global Balance Dashboard", layout="wide")


# Styling (Light Gray Theme)
# -----------------------------
st.markdown("""
<style>
    /* --- App background --- */
    .stApp {
        background-color: #f3f3f4;  /* Light Grey */
        color: #000000;
    }

    /* --- Top header style --- */
    .header {
        background-color: #d6d6d6;  /* Light Gray */
        padding: 14px 28px;
        border-bottom: 2px solid #ffffff;
        margin-bottom: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 0px 0px 12px 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .header h1 {
        margin: 0;
        color: #000000; /* Black text on light header */
        font-weight: 700;
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: #d6d6d6;  /* Light Gray */
        color: #000000;
        padding-top: 28px;
    }

    /* --- Navigation buttons --- */
    div[role="radiogroup"] label {
        display: block;
        background: #ffffff;        
        color: #000000 !important;  
        padding: 12px 16px;
        border-radius: 10px;
        margin: 8px 16px;
        font-weight: 600;
        cursor: pointer;
        border: 2px solid #d6d6d6;
        text-align: center;
        width: 85% !important;
        transition: background 0.3s, transform 0.2s, color 0.2s;
    }
    div[role="radiogroup"] label:hover {
        background: #b0b0b0;
        color: #ffffff !important;
        transform: translateY(-2px);
    }
    div[role="radiogroup"] label[aria-checked="true"] {
        background: #b0b0b0 !important;  
        color: #ffffff !important;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* --- Primary buttons (White with hover) --- */
    div.stButton > button {
        background-color: #ffffff;
        color: #000000;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: 600;
        border: 2px solid #b0b0b0;
        transition: background-color 0.2s, transform 0.2s, color 0.2s;
        margin: 6px auto;
    }
    div.stButton > button:hover {
        background-color: #b0b0b0;
        color: #ffffff;
        transform: translateY(-2px);
    }

    /* --- Inputs --- */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 2px solid #b0b0b0 !important;
    }

    /* --- Headings --- */
    h1, h2, h3 {
        color: #000000;
        font-weight: 700;
    }

    /* --- Card / iframe holder --- */
    .iframe-card {
        background: #ffffff;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    /* --- Feedback Table --- */
    .feedback-table {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .feedback-table th {
        background-color: #b0b0b0 !important;
        color: white !important;
        font-weight: bold;
        padding: 10px;
    }
    .feedback-table td {
        padding: 10px;
    }
    .feedback-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state for login/logout
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Sidebar Nav
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Dashboard", "Insight", "About", "Feedback"])

# -----------------------------
# Header
# -----------------------------
st.markdown(f"""
<div class="header">
  <h1>🌍 &nbsp; Global Balance</h1>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Pages
# -----------------------------
if page == "Login":
    st.markdown("## 🔑 Login Page")

    if st.session_state.logged_in:
        if st.button("🚪 Logout", key="logout_btn"):
            st.session_state.logged_in = False
            st.success("✅ Logged out successfully!")
            st.rerun()

    if not st.session_state.logged_in:
        username = st.text_input("Enter Username")
        password = st.text_input("Enter Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("✅ Login Successful!")
                st.rerun()
            else:
                st.error("❌ Invalid Username or Password")
    else:
        st.success("✅ You are already logged in.")

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

    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.markdown('<div class="feedback-table">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🗑️ Erase All Feedback"):
            os.remove("feedback.csv")
            st.warning("⚠️ All feedback has been erased.")
            st.rerun()
