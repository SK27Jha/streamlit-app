import streamlit as st
import pandas as pd
import os
from datetime import datetime

# File to store feedback
FEEDBACK_FILE = "feedback_responses.csv"

# --- Custom CSS ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1E1E2E;
        padding: 20px;
    }
    [data-testid="stSidebar"] h2 {
        color: #ffffff;
        font-size: 22px;
        text-align: center;
        margin-bottom: 20px;
    }
    .css-1kyxreq div {
        color: #ffffff !important;
        font-size: 18px !important;
        padding: 10px;
    }
    div[data-testid="stSidebarNav"] button[aria-selected="true"] {
        background-color: #007BFF !important;
        border-radius: 10px;
        color: white !important;
    }
    .logout-btn {
        position: absolute;
        top: 15px;
        right: 25px;
    }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Login", "Dashboard", "Insight", "About", "Feedback"])


# --- Top Section with Logout ---
col1, col2 = st.columns([8, 2])
with col1:
    st.title("🌍 Global Balance")
with col2:
    st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
    if st.button("Logout"):
        st.warning("🔒 You have logged out successfully.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- Pages ---
if menu == "Login":
    st.subheader("🔑 Login Page")
    st.text_input("Enter Username")
    st.text_input("Enter Password", type="password")
    st.button("Login")

elif menu == "Dashboard":
    st.subheader("📊 Dashboard")
    st.markdown("""
        <iframe title="Global Income Inequality Dahboard" 
        width="100%" height="500" 
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9" 
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)

elif menu == "Insight":
    st.subheader("📖 Insights from Dashboard")

    st.write("""
    ✅ **Key Takeaways**  
    - **Global Coverage**: Data spans **15 countries** with diverse income groups.  
    - **Inequality Snapshot**:  
        • Avg. Gini Index = **0.43**  
        • Max = **0.65**, Min = **0.20**  
    - **Income Distribution**:  
        • Avg. Income ≈ **35.43K USD**  
        • Population covered ≈ **172.23M**  
    - **Income Groups**:  
        • High Income: 28.9%  
        • Upper Middle: 24.2%  
        • Low Income: 23.6%  
        • Lower Middle: 23.3%  
    - **Top Performers**:  
        • Highest Avg. Income → **Saudi Arabia, Germany, Canada, US**  
        • Biggest inequality gap → **China, Mexico, India** (Top 10% share vs Bottom 10%).  
    - **Trends Over Time (2000–2023)**:  
        • Inequality fluctuates but general upward income growth trend.  
        • High-income countries show steadier Gini indexes, while middle/low-income fluctuate more.  
    """)

    st.info("📌 These insights are auto-generated from your dashboard visuals.")

elif menu == "About":
    st.subheader("ℹ️ About")
    st.write("""
    This dashboard is built to analyze **global income inequality trends**.  
    Features include:
    - Gini index monitoring  
    - Population vs income distribution  
    - Country & income group analysis  
    - Interactive Power BI reports  
    """)

elif menu == "Feedback":
    st.subheader("💬 Feedback")

    # Feedback Form
    feedback = st.text_area("Your feedback")
    rating = st.slider("Rate the dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)

    if st.button("Send Feedback"):
        # Save feedback to CSV
        new_feedback = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "feedback": feedback,
            "rating": rating
        }

        if os.path.exists(FEEDBACK_FILE):
            df = pd.read_csv(FEEDBACK_FILE)
            df = pd.concat([df, pd.DataFrame([new_feedback])], ignore_index=True)
        else:
            df = pd.DataFrame([new_feedback])

        df.to_csv(FEEDBACK_FILE, index=False)
        st.success("✅ Thank you! Your feedback has been recorded.")

    # Show Past Feedback
    if os.path.exists(FEEDBACK_FILE):
        st.markdown("### 📌 Recent Feedback")
        df = pd.read_csv(FEEDBACK_FILE)
        st.dataframe(df.tail(5))  # Show last 5 feedbacks
