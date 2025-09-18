# app.py
import streamlit as st
import pandas as pd
import time
import os
from datetime import datetime
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

# -----------------------------
# Styling (Global Animations & Transitions)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
    color: #000000;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Fade-in animation for all pages */
.main { animation: fadeIn 0.8s ease-in; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Metric bounce */
.stMetric { animation: bounceIn 1s ease; }
@keyframes bounceIn {
  0% { transform: scale(0.5); opacity: 0; }
  60% { transform: scale(1.1); opacity: 1; }
  100% { transform: scale(1); }
}

/* Button hover animation */
.stButton > button {
    transition: all 0.3s ease-in-out;
    border-radius: 12px;
    font-weight: 600;
}
.stButton > button:hover {
    transform: scale(1.05);
    background-color: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Helper: Load Lottie
# -----------------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animated number counter
def animated_number(value, duration=2):
    components.html(f"""
    <h2 id="num">0</h2>
    <script>
    let start = 0;
    let end = {value};
    let duration = {duration} * 1000;
    let range = end - start;
    let stepTime = Math.abs(Math.floor(duration / range));
    let obj = document.getElementById("num");
    let current = start;
    let timer = setInterval(function() {{
        current += 1;
        obj.innerHTML = current;
        if (current == end) clearInterval(timer);
    }}, stepTime);
    </script>
    """, height=50)

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Sidebar Navigation
# -----------------------------
if st.session_state.logged_in:
    page = st.sidebar.radio("Navigate", ["Dashboard", "Insight", "About", "Feedback"])
else:
    page = "Login"

# -----------------------------
# Login Page
# -----------------------------
if page == "Login":
    st.title("🔐 Login to Access Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("✅ Login Successful!")

            # 🎉 Success animation
            lottie_success = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
            st_lottie(lottie_success, height=200, key="login_success")

            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "Dashboard":
    st.title("📊 Global Income Inequality Dashboard")

    # Simulate "analyzing data"
    with st.spinner("🔍 Analyzing global inequality data..."):
        lottie_analysis = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_puciaact.json")
        st_lottie(lottie_analysis, height=250, key="data_analysis")
        time.sleep(2)

    # Progress bar
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
    st.success("✅ Analysis Complete")

    st.subheader("🌍 Key Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("🌎 Global Avg Gini Index")
        animated_number(39)

    with col2:
        st.write("⬆️ Highest Inequality (South Africa)")
        animated_number(63)

    with col3:
        st.write("⬇️ Lowest Inequality (Slovenia)")
        animated_number(24)

# -----------------------------
# Insight Page
# -----------------------------
elif page == "Insight":
    st.title("🔎 Insights")

    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
    if uploaded_file is not None:
        df_insight = pd.read_csv(uploaded_file)
        st.success("✅ CSV uploaded successfully!")
        st.balloons()
        st.write(df_insight.head())

    st.info("💡 Observations: Inequality varies significantly across regions...")

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
    st.title("ℹ️ About This Project")
    st.write("""
    This dashboard was built to explore **global income inequality** using data visualization.
    - 🎯 Objective: Understand inequality trends  
    - 🛠️ Tools: Streamlit, Pandas, Lottie animations  
    """)

# -----------------------------
# Feedback Page
# -----------------------------
elif page == "Feedback":
    st.title("📝 Share Your Feedback")

    feedback = st.text_area("💬 Your feedback here...")
    rating = st.slider("⭐ Rate the dashboard", 1, 5, 3)
    submitted = st.button("Submit Feedback")

    if submitted:
        if feedback.strip():
            # Save feedback (placeholder)
            lottie_thanks = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_touohxv0.json")
            st_lottie(lottie_thanks, height=200, key="thanks")
            st.success(f"✅ Thank you! Feedback saved with rating {rating}/5")
        else:
            st.error("⚠️ Feedback cannot be empty")
