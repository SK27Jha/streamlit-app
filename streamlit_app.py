# app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Global Balance Dashboard", layout="wide")

# -----------------------------
# Styling: app colors + nav buttons
# -----------------------------
st.markdown(
    """
    <style>
    /* --- App background & text --- */
    .stApp {
        background: linear-gradient(180deg, #f7f9fc 0%, #eef3f8 100%);
        color: #0f1724;
    }

    /* --- Top header style --- */
    .header {
        background-color: #ffffff;
        padding: 14px 28px;
        border-bottom: 1px solid rgba(16,24,40,0.06);
        box-shadow: 0 1px 0 rgba(16,24,40,0.02);
        margin-bottom: 18px;
    }
    .header h1 {
        margin: 0;
        color: #0f1724;
    }

    /* --- Sidebar container --- */
    section[data-testid="stSidebar"] {
        background: #0f1724;            /* deep navy */
        color: #ffffff;
        padding-top: 28px;
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] .css-1d391kg,
    section[data-testid="stSidebar"] .css-1fv8s86 {
        color: #ffffff !important;
    }

    /* --- Radio / nav options: make them look like buttons --- */
    div[role="radiogroup"] label,
    label[data-baseweb="radio"] {
        display: block;
        background: #142634;           /* default button bg */
        color: #cbd5e1 !important;     /* muted text */
        padding: 10px 14px;
        border-radius: 10px;
        margin: 6px 12px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.12s ease, background 0.12s ease;
        box-shadow: none;
        border: 1px solid rgba(255,255,255,0.04);
    }

    /* Hover state */
    div[role="radiogroup"] label:hover,
    label[data-baseweb="radio"]:hover {
        transform: translateY(-2px);
        background: #163447;
        color: #ffffff !important;
    }

    /* Selected state — multiple fallbacks for selectors */
    label[data-checked="true"],
    div[role="radiogroup"] label[aria-checked="true"],
    label[data-baseweb="radio"]:has(input:checked)
    {
        background: linear-gradient(90deg,#0073e6,#005bb5) !important;
        color: #ffffff !important;
        box-shadow: 0 6px 18px rgba(3,102,214,0.18);
        border: 1px solid rgba(0,82,180,0.9);
    }

    /* Ensure radio dot remains visible */
    div[role="radiogroup"] input[type="radio"] {
        accent-color: #ffffff;
    }

    /* --- Primary buttons in app --- */
    div.stButton > button {
        background: linear-gradient(90deg,#0073e6,#005bb5);
        color: #fff;
        padding: 8px 16px;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }
    div.stButton > button:hover {
        filter: brightness(0.95);
        transform: translateY(-2px);
    }

    /* Text area / inputs visual */
    textarea, input, .stTextInput>div>input {
        border-radius: 8px !important;
    }

    /* Page headings color */
    h1, h2, h3 {
        color: #0f1724;
    }

    /* Make the iframe area look card-like */
    .iframe-card {
        background: white;
        border-radius: 10px;
        padding: 8px;
        box-shadow: 0 6px 18px rgba(3,102,214,0.06);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar Nav (streamlit radio)
# -----------------------------
st.sidebar.title("Navigation")
# Using st.radio (styled above)
page = st.sidebar.radio("Go to", ["Login", "Dashboard", "Insight", "About", "Feedback"])

# -----------------------------
# Header (top area)
# -----------------------------
st.markdown(
    """
    <div class="header">
      <h1>🌍 &nbsp; Global Balance</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

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
    st.markdown(
        """
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Insight":
    st.markdown("## 🔎 Insights from Dashboard")
    st.markdown(
        """
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
        """
    )

elif page == "About":
    st.markdown("## ℹ️ About This Project")
    st.markdown(
        """
        ### 🌍 Global Balance – Income Inequality Dashboard  

        This project analyzes and visualizes global income inequality using interactive dashboards and highlights:

        - **Gini Index** — inequality metric.
        - **Average & Distribution of Income** across income groups.
        - **Top 10% vs Bottom 10% Share** — wealth concentration measure.
        - **Population vs Income Trends** across 2000–2023.

        **Tools:** Power BI (visuals) + Streamlit & Python (Pandas, Matplotlib/Plotly) for web integration.
        """
    )

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
            st.success("✅ Thank you! Your feedback has been saved.")
        else:
            st.error("⚠️ Please enter feedback before submitting.")
    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
