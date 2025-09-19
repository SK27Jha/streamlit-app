# app.py
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time

st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

# -----------------------------
# Function to embed Lottie animation
# -----------------------------
def lottie_embed(url, height=300):
    components.html(f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="{url}" background="transparent" 
                   speed="1" style="width:100%;height:{height}px;" 
                   loop autoplay>
    </lottie-player>
    """, height=height)

# -----------------------------
# Navigation Menu
# -----------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📈 Insights", "📊 Dashboard", "ℹ️ About", "📝 Feedback"])

# -----------------------------
# Home
# -----------------------------
if page == "🏠 Home":
    st.title("🌍 Global Income Inequality Dashboard")
    st.write("Welcome! This interactive dashboard helps visualize and analyze global income inequality trends.")

    # Professional global animation
    lottie_embed("https://lottie.host/f00cb39b-24e7-46c5-bf3c-7d7b7f4f1dbe/jdLxlYOnlW.json", height=280)

# -----------------------------
# Insights
# -----------------------------
elif page == "📈 Insights":
    st.header("📊 Key Insights from Data")

    st.markdown("""
    ### 🌟 Observations
    - Inequality varies significantly across regions.  
    - Gini index values highlight disparities in income distribution.  
    - The data helps policymakers, researchers, and students analyze inequality.  
    """)

    # Load CSV (replace with your actual file path if needed)
    try:
        df = pd.read_csv("global_inequality.csv")
        st.subheader("📂 Uploaded Data Snapshot")
        st.dataframe(df.head())
    except:
        st.error("CSV file not found. Please make sure `global_inequality.csv` is in the same directory.")

    # Insights animation
    lottie_embed("https://lottie.host/620ce553-3c84-41d0-a17c-4e06794860a6/qG9zDCJ3BJ.json", height=260)

# -----------------------------
# Dashboard
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

    # Professional Data Analysis Animation (team analyzing datasets)
    lottie_embed("https://lottie.host/ea0b15f3-7d47-4ac1-84ad-1f2a61d8b8e1/zXgPZbWqzM.json", height=280)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# About
# -----------------------------
elif page == "ℹ️ About":
    st.header("ℹ️ About This Project")
    st.write("""
    This dashboard was built to provide insights into global income inequality using interactive data visualization.  
    It integrates datasets, metrics, and animations to make the analysis more engaging.  

    **Tech Stack**:  
    - Python  
    - Streamlit  
    - Pandas  
    - HTML + Lottie animations  
    - Power BI
    """)

    # About animation
    lottie_embed("https://lottie.host/6a8a692f-5ab0-46a0-8197-2d3999d1f31d/cFF7L5CMsU.json", height=240)

# -----------------------------
# Feedback
# -----------------------------
elif page == "📝 Feedback":
    st.header("💬 Feedback")

    with st.form("feedback_form", clear_on_submit=True):
        feedback = st.text_area("Your feedback")
        rating = st.slider("Rate this Dashboard (1 = Poor, 5 = Excellent)", 1, 5, 3)
        submitted = st.form_submit_button("Send Feedback")

        if submitted:
            with st.spinner("📩 Submitting your feedback..."):
                time.sleep(2)

            st.success("🎉 Thank you for your valuable feedback!")
            lottie_embed("https://lottie.host/3d9a6bb8-0ecb-43c1-89dd-22d6b7eb5d65/lPuUqH9oXj.json", height=260)
            st.info("Your feedback helps improve this dashboard further 🚀")
