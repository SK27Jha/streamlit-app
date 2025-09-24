import streamlit as st
import pandas as pd
import os
from datetime import datetime
import streamlit.components.v1 as components
from openai import OpenAI

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
    st.session_state.page = "Login"
if "csv_data" not in st.session_state:
    st.session_state.csv_data = None

page = st.session_state.page

# -----------------------------
# Function for embedding Lottie animations
# -----------------------------
def lottie_embed(url, height=250):
    components.html(f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player 
        src="{url}"  
        background="transparent"  
        speed="1"  
        style="width:100%; height:{height}px; display:block; margin:auto;"  
        loop  
        autoplay>
    </lottie-player>
    """, height=height + 50)


# -----------------------------
# Global CSS Styling
# -----------------------------
st.markdown("""
<style>
/* Full-screen background */
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=1470&q=80');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    min-height: 100vh;
    color: white;
    position: relative;
    overflow: hidden;
}

/* Remove white header background */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* Overlay for readability */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.45);
    pointer-events: none;
    z-index: 0;
}

/* Glassmorphism cards */
.card, .stButton>button, .stTextInput, .stTextArea {
    background-color: rgba(255,255,255,0.85);
    color: black;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    backdrop-filter: blur(8px);
    position: relative;
    z-index: 1;
}

/* Metrics boxes */
.stMetric {
    background-color: rgba(255,255,255,0.85) !important;
    color: black !important;
    border-radius: 12px !important;
    padding: 15px !important;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
    position: relative;
    z-index: 1;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.7);
    color: white;
    backdrop-filter: blur(10px);
    min-height: 100vh;
}

/* Sidebar buttons */
.stButton>button {
    width: 100%;
    background-color: rgba(255,255,255,0.2);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: rgba(255,255,255,0.3);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Welcome👍")
pages = ["Login", "Dashboard", "Insights", "About", "Feedback","AI Assistance"]
for p in pages:
    if st.sidebar.button(p, use_container_width=True):
        st.session_state.page = p
        page = p

# -----------------------------
# Login Page
# -----------------------------
if page == "Login":
    st.markdown("## Login Page")
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json", height=200)

    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.success("Logged out successfully!")
            st.rerun()
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "Dashboard":
    st.markdown("## Dashboard Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Global Avg Gini Index", "38.5", "⬆️ 1.2%")
    with col2:
        st.metric("Highest Inequality", "South Africa", "+65.0 Gini")
    with col3:
        st.metric("Lowest Inequality", "Slovenia", "23.7 Gini")

    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=250)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true" style="position:relative; z-index:2;"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Insights Page
# -----------------------------
elif page == "Insights":
    st.markdown("## Data Insights")
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_jtbfg2nb.json", height=220)

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.csv_data = df
        st.markdown("### Raw Data Preview")
        st.dataframe(df)

        if "Country" in df.columns and "Gini Index" in df.columns:
            st.markdown("### Country-wise Gini Index")
            st.bar_chart(df.set_index("Country")["Gini Index"])

        if "Year" in df.columns:
            st.markdown("### Gini Index Trend Over Years")
            st.line_chart(df.groupby("Year")["Gini Index"].mean())

        st.markdown("### Quick Analysis")
        st.write(f"Number of countries: {df['Country'].nunique()}")
        st.write(f"Highest Gini Index: {df['Gini Index'].max()}")
        st.write(f"Lowest Gini Index: {df['Gini Index'].min()}")
        st.write(f"Average Gini Index: {round(df['Gini Index'].mean(),2)}")
    else:
     st.markdown(
    "<div style='color:white; font-weight:bold;'>Upload a CSV file to see insights.</div>",
    unsafe_allow_html=True
)

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
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

elif page == "📝 Feedback":
    st.markdown("## 📝 Feedback")
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_fcfjwiyb.json", height=220)

    csv_file = os.path.join(os.getcwd(), "feedback.csv")  # absolute path

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("💬 Your feedback")
        rating = st.slider("⭐ Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)
        submitted = st.form_submit_button("Send Feedback")

        if submitted:
            if feedback.strip():
                df_new = pd.DataFrame({
                    "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    "Feedback": [feedback],
                    "Rating": [rating],
                })
                df_new.to_csv(csv_file, mode='a', index=False, header=not os.path.exists(csv_file))
                st.success(f"✅ Thank you! Feedback saved with rating {rating}/5")
            else:
                st.error("⚠️ Please enter feedback before submitting.")

    # Download button outside form
    if os.path.exists(csv_file):
        with open(csv_file, "rb") as f:
            st.download_button(
                label="⬇️ Download All Feedback (CSV)",
                data=f,
                file_name="feedback.csv",
                mime="text/csv"
            )
