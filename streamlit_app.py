import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

# -----------------------------
# Function for embedding Lottie animations
# -----------------------------
def lottie_embed(url, height=250):
    components.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="{url}" background="transparent" speed="1" style="height: {height}px; margin: auto;" loop autoplay></lottie-player>
    """, height=height+50)

# -----------------------------
# Styling (White + Light Gray Theme)
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;  
        color: #000000;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("📌 Navigation")
pages = ["🔑 Login", "📊 Dashboard", "📈 Insights", "ℹ️ About", "📝 Feedback"]
page = st.sidebar.radio("Go to", pages)

# -----------------------------
# Login Page
# -----------------------------
if page == "🔑 Login":
    st.markdown("## 🔑 Login Page")
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_touohxv0.json", height=220)

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login"):
        if username.strip() and password.strip():
            st.success(f"✅ Welcome, {username}!")
            lottie_embed("https://assets1.lottiefiles.com/packages/lf20_q5pk6p1k.json", height=200)
        else:
            st.error("⚠️ Please enter both username and password.")

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "📊 Dashboard":
    st.markdown("## 📊 Dashboard Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🌎 Global Avg Gini Index", "38.5", "⬆️ 1.2%")
    with col2:
        st.metric("📈 Highest Inequality", "South Africa", "+65.0 Gini")
    with col3:
        st.metric("📉 Lowest Inequality", "Slovenia", "23.7 Gini")

    # Professional animation
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json", height=280)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Insights Page
# -----------------------------
elif page == "📈 Insights":
    st.markdown("## 📈 Data Insights")
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_jtbfg2nb.json", height=220)

    csv_path = r"C:\Users\ASUS\Downloads\global_income_inequality.csv"

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)

        st.markdown("### 📊 Raw Data Preview")
        st.dataframe(df)

        # Bar Chart
        st.markdown("### 📊 Country-wise Gini Index")
        st.bar_chart(df.set_index("Country")["Gini Index"])

        # Line Chart (if Year column exists)
        if "Year" in df.columns:
            st.markdown("### 📈 Gini Index Trend Over Years")
            st.line_chart(df.groupby("Year")["Gini Index"].mean())

        # Analysis
        st.markdown("### 🔎 Quick Analysis")
        st.write(f"✅ Number of countries in dataset: **{df['Country'].nunique()}**")
        st.write(f"📈 Highest Gini Index: **{df['Gini Index'].max()}**")
        st.write(f"📉 Lowest Gini Index: **{df['Gini Index'].min()}**")
        st.write(f"🌍 Average Gini Index: **{round(df['Gini Index'].mean(),2)}**")

    else:
        st.error(f"⚠️ CSV file not found at `{csv_path}`")


# -----------------------------
# About Page
# -----------------------------
elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This Project")
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_kyu7xb1v.json", height=220)

    st.markdown("""
    This project provides **insights into global income inequality**  
    using **Gini Index, data visualization, and interactive analysis**.

    ### 🎯 Objectives:
    - Track and analyze **income distribution across countries**
    - Provide **interactive dashboards** using Power BI
    - Highlight regions with **extreme inequality**
    - Gather **feedback for continuous improvement**

    ### 🛠 Methodology:
    - Data Cleaning & Preprocessing (CSV datasets)
    - Exploratory Data Analysis (EDA) using Python
    - Dashboard integration with **Power BI**
    - User feedback integration for better insights

    ### 🌍 Why It Matters?
    Income inequality affects **social stability, economic growth, and global development**.  
    This dashboard aims to make inequality **easy to understand and act upon**.
    """)

# -----------------------------
# Feedback Page
# -----------------------------
elif page == "📝 Feedback":
    st.markdown("## 📝 Feedback")
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_fcfjwiyb.json", height=220)

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("💬 Your feedback")
        rating = st.slider("⭐ Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)
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
                lottie_embed("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=200)
            else:
                st.error("⚠️ Please enter feedback before submitting.")
