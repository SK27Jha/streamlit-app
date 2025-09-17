import streamlit as st
import pandas as pd
import os
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Global Balance Dashboard", layout="wide")

# -----------------------------
# Custom Styling (Theme + Nav Buttons)
# -----------------------------
page_bg_css = """
<style>
    /* App background */
    .stApp {
        background-color: #f9fafc; /* light background */
        color: #222222; /* dark text */
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #1a2b48; /* dark navy */
    }

    /* Sidebar radio buttons (navigation) */
    div[role="radiogroup"] label {
        background-color: #2c3e5b;
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        margin-bottom: 6px;
        font-weight: 500;
        cursor: pointer;
    }

    /* Highlight selected navigation button */
    div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) {
        background-color: #0073e6 !important;
        color: white !important;
        font-weight: bold;
        border: 1px solid #005bb5;
    }

    /* Sidebar title */
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
        color: white !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #0073e6;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #005bb5;
        color: white;
    }

    /* Headings */
    h1, h2, h3 {
        color: #1a2b48;
    }
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Dashboard", "Insight", "About", "Feedback"])

# -----------------------------
# Login Page
# -----------------------------
if page == "Login":
    st.markdown("<h1 style='text-align: center;'>🌍 Global Balance</h1>", unsafe_allow_html=True)
    st.subheader("🔑 Login Page")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login", use_container_width=True):
        if username == "admin" and password == "1234":
            st.success("✅ Login Successful!")
        else:
            st.error("❌ Invalid Username or Password")

# -----------------------------
# Dashboard Page (Power BI iframe)
# -----------------------------
elif page == "Dashboard":
    st.markdown("## 📊 Dashboard")
    st.markdown(
        """
        <iframe title="Global Income Inequality Dashboard" width="100%" height="600" 
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9" 
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Insight Page
# -----------------------------
elif page == "Insight":
    st.subheader("🔎 Insights from Dashboard")

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
    """)

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
    st.subheader("ℹ️ About This Project")

    st.markdown("""
    ### 🌍 Global Balance – Income Inequality Dashboard  

    This project is designed to **analyze and visualize global income inequality** using interactive dashboards.  
    It brings together multiple metrics such as:  

    - **Gini Index** → Measures inequality in income distribution.  
    - **Average & Distribution of Income** → Across different income groups.  
    - **Top 10% vs Bottom 10% Share** → Identifies concentration of wealth.  
    - **Population vs Income Trends** → How demographics impact inequality.  

    ### 🎯 Objective
    - Provide policymakers, researchers, and analysts with clear insights into global inequality.  
    - Track **changes over time (2000–2023)** to identify trends.  
    - Highlight **country-level differences** between high, middle, and low-income groups.  

    ### 🛠️ Tools Used
    - **Power BI** → For dashboard design & visuals.  
    - **Streamlit & Python (Pandas, Matplotlib/Plotly)** → For web app integration.  

    ---
    ✅ *This platform aims to make global inequality data more **transparent, interactive, and actionable.***
    """)

# -----------------------------
# Feedback Page (with CSV Save)
# -----------------------------
elif page == "Feedback":
    st.subheader("📝 Feedback")

    feedback = st.text_area("Your feedback")
    rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5)

    if st.button("Send Feedback"):
        if feedback:
            # Save feedback into CSV
            feedback_data = {
                "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Feedback": [feedback],
                "Rating": [rating]
            }

            df_new = pd.DataFrame(feedback_data)

            if os.path.exists("feedback.csv"):
                df_existing = pd.read_csv("feedback.csv")
                df = pd.concat([df_existing, df_new], ignore_index=True)
            else:
                df = df_new

            df.to_csv("feedback.csv", index=False)

            st.success("✅ Thank you for your feedback! It has been recorded.")
            st.write("**Your Feedback:**", feedback)
            st.write("**Your Rating:**", rating, "⭐")
        else:
            st.error("⚠️ Please enter feedback before submitting.")

    # Show previous feedback if available
    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.dataframe(df)
