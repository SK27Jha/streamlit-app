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
if "page" not in st.session_state:
    st.session_state.page = "🔑 Login"
if "csv_data" not in st.session_state:
    st.session_state.csv_data = None

# -----------------------------
# Function for embedding Lottie animations
# -----------------------------
def lottie_embed(url, height=250):
    components.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="{url}" background="transparent" speed="1" style="height: {height}px; margin: auto;" loop autoplay></lottie-player>
    """, height=height+50)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    /* Main office image with people working */
    background-image: 
        url('https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=1470&q=80'),
        url('https://images.unsplash.com/photo-1581091870626-87e7488dc9d8?auto=format&fit=crop&w=1470&q=80');
    background-size: cover, cover;
    background-position: center, center;
    background-attachment: fixed;
    color: white;
    position: relative;
}

/* Optional overlay for global finance graphs */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background-image: url('https://images.unsplash.com/photo-1581091870626-87e7488dc9d8?auto=format&fit=crop&w=1470&q=80');
    background-size: cover;
    opacity: 0.25;  /* transparency for overlay */
    pointer-events: none;
}

/* Glassmorphism cards */
.card {
    background-color: rgba(0,0,0,0.55);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    backdrop-filter: blur(8px);
    color: white;
}

/* Sidebar buttons */
.sidebar-btn-container button {
    background-color: rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)




# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Welcome 👍")
st.sidebar.markdown('<div class="sidebar-btn-container">', unsafe_allow_html=True)

if st.sidebar.button("🔑 Login", use_container_width=True):
    st.session_state.page = "🔑 Login"
if st.sidebar.button("📊 Dashboard", use_container_width=True):
    st.session_state.page = "📊 Dashboard"
if st.sidebar.button("📈 Insights", use_container_width=True):
    st.session_state.page = "📈 Insights"
if st.sidebar.button("ℹ️ About", use_container_width=True):
    st.session_state.page = "ℹ️ About"
if st.sidebar.button("📝 Feedback", use_container_width=True):
    st.session_state.page = "📝 Feedback"

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Page Rendering
# -----------------------------
page = st.session_state.page

# ---------------- Login Page ----------------
if page == "🔑 Login":
    st.markdown("## 🔑 Login Page")
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json", height=200)

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

# ---------------- Dashboard ----------------
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

# ---------------- Insights ----------------
elif page == "📈 Insights":
    st.markdown("## 📈 Data Insights")
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_jtbfg2nb.json", height=220)

    uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.csv_data = df  # Save CSV in session state
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

# ---------------- About ----------------
elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This Project")
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_kyu7xb1v.json", height=220)
    st.markdown("""
    ### Project Overview
    This project provides **insights into global income inequality** using data analysis, visualizations, and interactive dashboards.

    ### Objectives
    - Analyze **income distribution across countries**.
    - Highlight **countries with extreme inequality**.
    - Provide **interactive dashboards** for exploration.
    - Enable **data-driven decisions** and policy recommendations.

    ### Data Sources
    - Global Gini Index data.
    - World Bank and UN datasets for population and income.
    - Power BI dashboards for visual analysis.

    ### Methodology
    - Data cleaning and aggregation.
    - Calculating metrics like **average Gini Index, highest and lowest values**.
    - Visualizations using **line charts, bar charts, and interactive dashboards**.
    - Feedback collection for continuous improvement.

    ### Insights
    - Some countries show consistently high inequality (e.g., South Africa).
    - Others maintain low inequality (e.g., Slovenia).
    - Tracking trends over years helps identify **improvements or declines**.
    """)

# ---------------- Feedback ----------------
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

                csv_file = "feedback.csv"

                if os.path.exists(csv_file):
                    df_existing = pd.read_csv(csv_file)
                    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                else:
                    df_combined = df_new

                df_combined.to_csv(csv_file, index=False)
                st.success(f"✅ Thank you! Feedback saved with rating {rating}/5")
            else:
                st.error("⚠️ Please enter feedback before submitting.")

    # Show Download button if feedback.csv exists
    if os.path.exists("feedback.csv"):
        with open("feedback.csv", "rb") as f:
            st.download_button(
                label="⬇️ Download All Feedback (CSV)",
                data=f,
                file_name="feedback.csv",
                mime="text/csv"
            )
