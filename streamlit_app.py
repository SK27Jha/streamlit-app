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

elif page == "🔎 Insight":
    st.markdown("## 🔎 Insights")
    
    # Lottie animation
    lottie_embed("https://assets9.lottiefiles.com/packages/lf20_fcfjwiyb.json", height=200)
    
    # Key Observations
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
    
    # Why it matters
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 Why It Matters")
    st.write("""
    Understanding income inequality helps policymakers, researchers, and organizations  
    design **targeted solutions** for inclusive growth and sustainable development.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Dataset Insights
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Dataset Insights")

    csv_path = "a4763003-e63f-4c5f-a0ae-500467ce4b8c.csv"
    df_insight = None

    # Upload option (overrides local CSV)
    uploaded_file = st.file_uploader("Upload CSV file (optional)", type=["csv"])
    
    if uploaded_file:
        df_insight = pd.read_csv(uploaded_file)
        st.success("✅ CSV uploaded successfully!")
    elif os.path.exists(csv_path):
        df_insight = pd.read_csv(csv_path)
        st.info(f"⚠️ Loaded local CSV: {csv_path}")
    else:
        st.warning("⚠️ No CSV found. Please upload a CSV to view dataset insights.")

    if df_insight is not None:
        st.dataframe(df_insight, use_container_width=True)
        st.markdown("---")
        st.write("### 📈 Summary Metrics")
        numeric_cols = df_insight.select_dtypes(include=['int64', 'float64']).columns
        if numeric_cols.any():
            for col in numeric_cols:
                st.metric(f"{col} Average", f"{df_insight[col].mean():.2f}")
        else:
            st.info("No numeric columns to display metrics.")
    
    st.markdown('</div>', unsafe_allow_html=True)

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
