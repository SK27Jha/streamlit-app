import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

# -----------------------------
# Function for embedding Lottie animations
# -----------------------------
def lottie_embed(url, height=250):
    components.html(f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="{url}" background="transparent" speed="1" 
        style="width: 100%; height: {height}px;" loop autoplay></lottie-player>
    """, height=height)

# -----------------------------
# Professional Animations
# -----------------------------
ANIMATIONS = {
    "login": "https://lottie.host/009d5cf4-b09b-47c5-b214-4a7cf00ed82a/1utj6oOfLP.json",
    "dashboard": "https://lottie.host/91c67f5b-73b3-4714-a0c8-18f4076b6f7f/uFzNEmYxY8.json",
    "insight": "https://lottie.host/657a01e7-84df-4c17-9c3c-29d942f9d2d6/v3RZ0JZTHP.json",
    "about": "https://lottie.host/234f4e19-5b64-40f5-9ec0-f3c84538c13b/1G83DYcG9B.json",
    "feedback": "https://lottie.host/778c55a6-7205-4ef0-86f0-b4cb2bb9a57b/TK3fxVUl56.json",
    "confetti": "https://lottie.host/11653d6a-389b-4a24-8f7e-4a1c885bf1c1/lMExQ60iTg.json"
}

# -----------------------------
# Styling (Professional White + Blue Theme)
# -----------------------------
st.markdown("""
<style>
.stApp { background-color: #ffffff; color: #000000; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.header { background: linear-gradient(90deg, #274c77, #6096ba); padding: 20px 28px; border-radius: 0px 0px 14px 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.25); color: white; }
.header h1 { margin: 0; font-weight: 900; font-size: 34px; }
.tagline { font-size: 18px; font-style: italic; margin-top: 6px; opacity: 0.9; }
section[data-testid="stSidebar"] { background-color: #f9f9f9; border-right: 2px solid #d3d3d3; }
div[role="radiogroup"] label { display: block; background: #ffffff; color: #274c77 !important; padding: 14px; border-radius: 12px; margin: 10px; font-weight: 600; border: 2px solid #274c77; text-align: center; }
div[role="radiogroup"] label:hover { background: #274c77; color: #ffffff !important; transform: translateY(-3px) scale(1.02); }
div[role="radiogroup"] label[aria-checked="true"] { background: #274c77 !important; color: #ffffff !important; border-left: 6px solid #ff6f61; }
div.stButton > button { background-color: #ffffff; color: #274c77; border-radius: 10px; padding: 10px 20px; font-weight: 700; border: 2px solid #274c77; transition: all 0.3s ease-in-out; }
div.stButton > button:hover { background-color: #274c77; color: #ffffff; transform: translateY(-3px) scale(1.05); }
textarea, input, .stTextInput>div>input { border-radius: 10px !important; border: 2px solid #274c77 !important; padding: 8px !important; }
.card { background: #ffffff; border-radius: 14px; padding: 24px; margin: 16px 0; box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.feedback-table { border-radius: 12px; overflow: hidden; box-shadow: 0 6px 16px rgba(0,0,0,0.12); }
.feedback-table th { background-color: #274c77 !important; color: white !important; font-weight: bold; padding: 12px; }
.feedback-table td { padding: 10px; }
.feedback-table tr:nth-child(even) { background-color: #f2f2f2; }
.stMetric { background: #ffffff; border-radius: 12px; padding: 14px; box-shadow: 0 4px 16px rgba(0,0,0,0.12); text-align: center; }
.stMetric:hover { transform: translateY(-3px) scale(1.03); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
#MainMenu, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Sidebar Nav
# -----------------------------
st.sidebar.title("🌍 Navigation")
page = st.sidebar.radio("Go to", ["🔑 Login", "📊 Dashboard", "🔎 Insight", "ℹ️ About", "📝 Feedback"])

# -----------------------------
# Header
# -----------------------------
st.markdown(f"""
<div class="header">
  <h1>🌍 Global Income Inequality Dashboard</h1>
  <p class="tagline">Tracking inequality trends across countries in real-time.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Pages
# -----------------------------
if page == "🔑 Login":
    st.markdown("## 🔑 Login Page")
    lottie_embed(ANIMATIONS["login"], height=220)

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
                lottie_embed(ANIMATIONS["confetti"], height=200)  # 🎉 Confetti animation
                st.rerun()
            else:
                st.error("❌ Invalid Username or Password")
    else:
        st.success("✅ You are already logged in.")

elif page == "📊 Dashboard":
    st.markdown("## 📊 Dashboard Overview")
    lottie_embed(ANIMATIONS["dashboard"], height=250)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🌎 Global Avg Gini Index", "38.5", "⬆️ 1.2%")
    with col2:
        st.metric("📈 Highest Inequality", "South Africa", "+65.0 Gini")
    with col3:
        st.metric("📉 Lowest Inequality", "Slovenia", "23.7 Gini")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "🔎 Insight":
    st.markdown("## 🔎 Insights")
    lottie_embed(ANIMATIONS["insight"], height=220)

    if os.path.exists("data.csv"):  # Attach your CSV here
        df = pd.read_csv("data.csv")
        st.subheader("📂 Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("📊 Basic Statistics")
        st.write(df.describe())

        # Example visualization
        if "Country" in df.columns and "Gini" in df.columns:
            st.bar_chart(df.set_index("Country")["Gini"].head(10))
    else:
        st.warning("⚠️ No data.csv file found. Please upload your dataset.")

elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This Project")
    lottie_embed(ANIMATIONS["about"], height=220)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌍 Project Purpose")
    st.write("""
    This dashboard is built to analyze and visualize **global income inequality trends**.  
    It helps researchers, policymakers, and students gain actionable insights.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📝 Feedback":
    st.header("💬 Feedback")
    lottie_embed(ANIMATIONS["feedback"], height=200)

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("Your feedback")
        rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)
        submitted = st.form_submit_button("Send Feedback")

        if submitted:
            with st.spinner("📩 Submitting your feedback..."):
                time.sleep(2)

            # Save feedback
            new_entry = pd.DataFrame([[feedback, rating]], columns=["Feedback", "Rating"])
            if os.path.exists("feedback.csv"):
                old = pd.read_csv("feedback.csv")
                df = pd.concat([old, new_entry], ignore_index=True)
            else:
                df = new_entry
            df.to_csv("feedback.csv", index=False)

            st.success("🎉 Thank you for your valuable feedback!")
            lottie_embed(ANIMATIONS["confetti"], height=200)  # 🎉 Confetti

    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.markdown('<div class="feedback-table">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        avg_rating = df["Rating"].mean()
        st.metric("⭐ Average Rating", f"{avg_rating:.2f} / 5")
