import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

# -----------------------------
# Function for embedding Lottie animations
# -----------------------------
def lottie_embed(url, height=250):
    components.html(f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="{url}" background="transparent" 
                   speed="1" style="width:100%;height:{height}px;" 
                   loop autoplay>
    </lottie-player>
    """, height=height)

# -----------------------------
# Styling (White + Animations)
# -----------------------------
st.markdown("""
<style>
/* --- App background --- */
.stApp { background-color: #ffffff; color: #000000; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; transition: background 0.5s ease-in-out; }
/* --- Top navigation header --- */
.header { background: linear-gradient(90deg, #3d6188, #6b9bd1); padding: 20px 28px; border-radius: 0px 0px 14px 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.25); color: white; transition: all 0.4s ease-in-out; animation: fadeSlide 1s ease-in-out; }
.header:hover { transform: scale(1.02); box-shadow: 0 10px 28px rgba(0,0,0,0.3); }
.header h1 { margin: 0; font-weight: 900; font-size: 36px; }
.tagline { font-size: 18px; font-style: italic; margin-top: 6px; opacity: 0.9; }
/* --- Sidebar --- */
section[data-testid="stSidebar"] { background-color: #f8f9fa; color: #000000; padding-top: 28px; border-right: 2px solid #d3d3d3; }
div[role="radiogroup"] label { display: block; background: #ffffff; color: #3d6188 !important; padding: 14px 18px; border-radius: 12px; margin: 10px 16px; font-weight: 600; cursor: pointer; border: 2px solid #3d6188; text-align: center; width: 85% !important; transition: all 0.4s ease-in-out; animation: fadeSlide 0.8s ease-in-out; }
div[role="radiogroup"] label:hover { background: #3d6188; color: #ffffff !important; transform: translateY(-3px) scale(1.02); box-shadow: 0 6px 16px rgba(0,0,0,0.2); }
div[role="radiogroup"] label[aria-checked="true"] { background: #3d6188 !important; color: #ffffff !important; border-left: 6px solid #ff6f61; box-shadow: 0 8px 20px rgba(0,0,0,0.25); }
/* --- Buttons --- */
div.stButton > button { background-color: #ffffff; color: #3d6188; border-radius: 10px; padding: 10px 20px; font-weight: 700; border: 2px solid #3d6188; transition: all 0.4s ease-in-out; margin: 8px auto; display: block; animation: fadeSlide 1s ease-in-out; }
div.stButton > button:hover { background-color: #3d6188; color: #ffffff; transform: translateY(-4px) scale(1.05); box-shadow: 0 6px 18px rgba(0,0,0,0.25); }
/* --- Inputs --- */
textarea, input, .stTextInput>div>input { border-radius: 10px !important; border: 2px solid #3d6188 !important; padding: 8px !important; transition: all 0.3s ease-in-out; animation: fadeSlide 0.8s ease-in-out; }
textarea:focus, input:focus, .stTextInput>div>input:focus { border-color: #6b9bd1 !important; box-shadow: 0 0 10px #6b9bd1; }
/* --- Card styling --- */
.card { background: #ffffff; border-radius: 14px; padding: 24px; margin: 16px 0; box-shadow: 0 6px 20px rgba(0,0,0,0.12); transition: all 0.4s ease-in-out; animation: fadeSlide 1s ease-in-out; }
.card:hover { transform: translateY(-4px) scale(1.02); box-shadow: 0 10px 28px rgba(0,0,0,0.25); }
.card h3 { margin-top: 0; color: #3d6188; }
/* --- Feedback Table --- */
.feedback-table { border-radius: 12px; overflow: hidden; box-shadow: 0 6px 16px rgba(0,0,0,0.12); transition: all 0.3s ease-in-out; animation: fadeSlide 1s ease-in-out; }
.feedback-table th { background-color: #3d6188 !important; color: white !important; font-weight: bold; padding: 12px; }
.feedback-table td { padding: 10px; transition: all 0.2s ease-in-out; }
.feedback-table tr:nth-child(even) { background-color: #f2f2f2; }
.feedback-table tr:hover td { background-color: #dce6f1; transform: scale(1.01); }
/* --- Metrics --- */
.stMetric { background: #ffffff; border-radius: 12px; padding: 14px; box-shadow: 0 4px 16px rgba(0,0,0,0.12); text-align: center; transition: all 0.4s ease-in-out; animation: fadeSlide 1s ease-in-out; }
.stMetric:hover { transform: translateY(-3px) scale(1.03); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
/* --- Animations --- */
@keyframes fadeSlide { 0% { opacity: 0; transform: translateY(15px); } 100% { opacity: 1; transform: translateY(0); } }
/* --- Remove footer --- */
#MainMenu, footer {visibility: hidden;}
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
st.sidebar.title("🌍 Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["🔑 Login", "📊 Dashboard", "🔎 Insight", "ℹ️ About", "📝 Feedback"]
)

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

elif page == "📊 Dashboard":
    st.markdown("## 📊 Dashboard Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🌎 Global Avg Gini Index", "38.5", "⬆️ 1.2%")
    with col2:
        st.metric("📈 Highest Inequality", "South Africa", "+65.0 Gini")
    with col3:
        st.metric("📉 Lowest Inequality", "Slovenia", "23.7 Gini")

    # Animation
    lottie_embed("https://assets4.lottiefiles.com/packages/lf20_sF5S5j.json", height=250)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "🔎 Insight":
    st.markdown("## 🔎 Insights")
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_fcfjwiyb.json", height=200)

    # Key Observations Card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Key Observations")
    st.write("""
    - Countries with **higher Gini Index** show **greater inequality**.  
    - Developed nations often have **lower inequality** but slower improvement.  
    - Developing countries display **wider income gaps** due to uneven distribution.  
    - Population growth in some regions correlates with **higher inequality trends**.  
    - Wealth concentration is highest in the **top 10%**, especially in emerging markets.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Why It Matters Card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 Why It Matters")
    st.write("""
    Understanding income inequality helps policymakers, researchers, and organizations  
    design **targeted solutions** for inclusive growth and sustainable development.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---- Dataset Insights ----
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Dataset Insights")

    csv_path = "a4763003-e63f-4c5f-a0ae-500467ce4b8c.csv"  # place CSV in same folder as app
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df_insight = pd.read_csv(uploaded_file)
        st.success("✅ CSV uploaded successfully!")
    elif os.path.exists(csv_path):
        df_insight = pd.read_csv(csv_path)
        st.info(f"⚠️ Loaded local CSV: {csv_path}")
    else:
        st.warning("⚠️ No CSV found. Please upload a CSV to view dataset insights.")
        df_insight = None

    if df_insight is not None:
        st.dataframe(df_insight, use_container_width=True)
        st.markdown("---")
        st.write("### 📈 Summary Metrics")
        for col in df_insight.select_dtypes(include=['int64', 'float64']).columns:
            st.metric(f"{col} Average", f"{df_insight[col].mean():.2f}")

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This Project")
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_xlmz9xwm.json", height=220)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌍 Global  Income Inequality Dashboard")
    st.write("""
    This project is designed to **analyze and visualize global income inequality**.  
    It combines interactive dashboards with powerful analytics to highlight inequality patterns.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎯 Objectives")
    st.write("""
    - Measure **income inequality using Gini Index**.  
    - Compare **top 10% vs bottom 10% income share**.  
    - Track **global and country-level changes (2000–2023)**.  
    - Provide actionable insights for **researchers, students, and policymakers**.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛠️ Tools Used")
    st.write("""
    - **Power BI** → For interactive dashboard visuals.  
    - **Streamlit & Python (Pandas)** → For web app integration.  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📝 Feedback":
    st.markdown("## 📝 Feedback")
    lottie_embed("https://assets1.lottiefiles.com/private_files/lf30_tjcwuzpm.json", height=180)

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
                lottie_embed("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=200)
            else:
                st.error("⚠️ Please enter feedback before submitting.")

    if os.path.exists("feedback.csv"):
        st.markdown("---")
        st.subheader("📂 Previous Feedback")
        df = pd.read_csv("feedback.csv")
        st.markdown('<div class="feedback-table">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        avg_rating = df["Rating"].mean()
        st.metric("⭐ Average Rating", f"{avg_rating:.2f} / 5")

        if st.button("🗑️ Erase All Feedback"):
            os.remove("feedback.csv")
            st.warning("⚠️ All feedback has been erased.")
            st.rerun()


   
