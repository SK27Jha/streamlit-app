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
# Initialize session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
# -----------------------------
# Centered Navigation Buttons
# -----------------------------
st.markdown("""
<style>
.nav-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
}
div.stButton > button:first-child {
    background-color: #4CAF50;
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 160px;
    font-size: 15px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #45a049;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Create button row
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🔑 Login"):
        st.session_state.page = "login"
with col2:
    if st.button("📊 Dashboard"):
        st.session_state.page = "dashboard"
with col3:
    if st.button("📈 Insights"):
        st.session_state.page = "insights"
with col4:
    if st.button("ℹ️ About"):
        st.session_state.page = "about"
with col5:
    if st.button("📝 Feedback"):
        st.session_state.page = "feedback"
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Page Routing
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"

page = st.session_state.page

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Welcome👍")


if page == "🔑 Login":
    st.markdown("## 🔑 Login Page")
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json", height=200)  # login animation

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
                lottie_embed("https://assets2.lottiefiles.com/private_files/lf30_jsgzryzx.json", height=200)  # success animation
                st.rerun()
            else:
                st.error("❌ Invalid Username or Password")
    else:
        st.success("✅ You are already logged in.")
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

    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=250)

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

    uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.markdown("### 📊 Raw Data Preview")
        st.dataframe(df)

        if "Country" in df.columns and "Gini Index" in df.columns:
            st.markdown("### 📊 Country-wise Gini Index")
            st.bar_chart(df.set_index("Country")["Gini Index"])

        if "Year" in df.columns:
            st.markdown("### 📈 Gini Index Trend Over Years")
            st.line_chart(df.groupby("Year")["Gini Index"].mean())

        st.markdown("### 🔎 Quick Analysis")
        st.write(f"✅ Number of countries: **{df['Country'].nunique()}**")
        st.write(f"📈 Highest Gini Index: **{df['Gini Index'].max()}**")
        st.write(f"📉 Lowest Gini Index: **{df['Gini Index'].min()}**")
        st.write(f"🌍 Average Gini Index: **{round(df['Gini Index'].mean(),2)}**")
    else:
        st.info("👆 Please upload a CSV file to see insights.")

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
                    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                else:
                    df_combined = df_new

                df_combined.to_csv("feedback.csv", index=False)
                
                st.success(f"✅ Thank you! Feedback saved with rating {rating}/5")
                
            else:
                st.error("⚠️ Please enter feedback before submitting.")
