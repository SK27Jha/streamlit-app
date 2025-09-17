# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global income inequality Dashboard", layout="wide")

# -----------------------------
# Styling: Using your new color palette
# -----------------------------
st.markdown("""
<style>
    /* --- App background & overall text color --- */
    .stApp {
        background-color: #FDEBD0;  /* cream lightest background */
        color: #0f1724;
    }

    /* --- Top header style --- */
    .header {
        background-color: #DC143C;  /* primary accent */
        padding: 14px 28px;
        border-bottom: 2px solid #F75270;
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #FFFFFF;
    }

    /* --- Sidebar container --- */
    section[data-testid="stSidebar"] {
        background-color: #DC143C;  /* primary accent */
        color: #FFFFFF;
        padding-top: 28px;
    }

    /* Sidebar title text color */
    section[data-testid="stSidebar"] .css-1d391kg,
    section[data-testid="stSidebar"] .css-1fv8s86 {
        color: #FFFFFF !important;
    }

    /* --- Navigation radio buttons styling --- */
    div[role="radiogroup"] label,
    label[data-baseweb="radio"] {
        display: block;
        background: #F7CAC9;           /* soft pink default */
        color: #0f1724 !important;     /* dark text for contrast */
        padding: 10px 14px;
        border-radius: 10px;
        margin: 6px 12px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        border: 1px solid #F75270;     /* border with secondary highlight */
    }

    /* Hover state for nav buttons */
    div[role="radiogroup"] label:hover,
    label[data-baseweb="radio"]:hover {
        background: #F75270;
        color: #FFFFFF !important;
        transform: translateY(-2px);
    }

    /* Selected nav button state */
    label[data-checked="true"],
    div[role="radiogroup"] label[aria-checked="true"],
    label[data-baseweb="radio"]:has(input:checked) {
        background: #DC143C !important;
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* Primary buttons in app */
    div.stButton > button {
        background-color: #DC143C;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
        border: none;
        transition: background-color 0.2s, transform 0.2s;
    }

    div.stButton > button:hover {
        background-color: #F75270;
        transform: translateY(-2px);
    }

    /* Inputs, text areas etc */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
        border: 1px solid #DC143C !important;
    }

    /* Headings color */
    h1, h2, h3 {
        color: #DC143C;
    }

    /* Card styling for iframe or content area */
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
# Header (top area)
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
    if st.button("Login", use_container_width=False):
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
        ### 📌 Key Findings

        - **Gini Index**
          - Average Gini Index across countries is around **0.43**.
          - Ranges from **0.20 (low inequality)** to **0.65 (high inequality)**.
        
        - **Income Distribution**
          - High Income group countries dominate with ~29%.
          - Upper Middle, Lower Middle, and Low Income countries share the rest almost equally.
        
        - **Top vs Bottom 10%**
          - The top 10% income share averages **40.20%**.
          - The bottom 10% income share averages only **2.99%**.
          - This highlights a **huge inequality gap**.
        
        - **Country-Level Observations**
          - Saudi Arabia, Germany, and Canada report high average incomes.
          - Countries like India, Mexico, and Nigeria show **higher inequality levels**.

        - **Trends Over Time (2000–2023)**
          - Fluctuations in Gini Index, but overall inequality persists.
          - Income growth is seen in high-income countries compared to low-income nations.

        ---
        ✅ These insights help in identifying **global inequality trends** and provide a base for further policy decisions.
    """, unsafe_allow_html=True)

elif page == "About":
    st.markdown("## ℹ️ About This Project")
    st.markdown("""
        **Global Balance – Income Inequality Dashboard**  

        An interactive platform built to visualize and analyze global income inequality. Highlights include:

        - **Gini Index**, **income distribution**, **top & bottom income shares**, and **population trends**.
        - Data from 2000-2023 to capture long-term trends.
        - Designed for policymakers, researchers, and anyone interested in global economic equity.

        Built using Power BI + Streamlit & Python (Pandas, etc).
    """, unsafe_allow_html=True)

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

