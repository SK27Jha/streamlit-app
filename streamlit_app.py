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
    /* Equal Sidebar Buttons */
    .sidebar-btn-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .sidebar-btn-container button {
        width: 100% !important;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        color: #333;
        cursor: pointer;
    }
    .sidebar-btn-container button:hover {
        background-color: #e6e6e6;
        border-color: #bbb;
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
if st.sidebar.button("🤖 AI Assistance", use_container_width=True):
    st.session_state.page = "🤖 AI Assistance"
if st.sidebar.button("📝 Feedback", use_container_width=True):
    st.session_state.page = "📝 Feedback"

st.sidebar.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Page Rendering
# -----------------------------
page = st.session_state.page

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
                lottie_embed("https://assets2.lottiefiles.com/private_files/lf30_jsgzryzx.json", height=200)
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

    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json", height=250)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <iframe title="Global Income Inequality Dashboard" width="100%" height="650"
        src="https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"
        frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

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

 
import openai

# Initialize API key
openai.api_key = "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"

elif page == "🤖 AI Assistance":
    st.markdown("## 🤖 AI Assistance")
    lottie_embed("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json", height=220)

    st.info("💡 Ask me anything about this dashboard, uploaded CSV data, or inequality insights.")

    # File uploader for CSV
    uploaded_csv = st.file_uploader("📂 (Optional) Upload CSV for AI to analyze", type=["csv"])

    df = None
    if uploaded_csv is not None:
        df = pd.read_csv(uploaded_csv)
        st.success(f"✅ CSV loaded with {df.shape[0]} rows and {df.shape[1]} columns")
        st.dataframe(df.head())

    # User query box
    user_query = st.text_area("💬 Enter your question here:")

    if st.button("Get Answer"):
        if user_query.strip():
            with st.spinner("🤖 Thinking..."):
                try:
                    context = ""
                    if df is not None:
                        # Give AI context about dataset
                        context = f"Dataset columns: {list(df.columns)}. Example rows: {df.head(5).to_dict()}"

                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are an AI assistant that analyzes a Global Income Inequality Dashboard. "
                                           "If a CSV dataset is provided, use it to answer questions based on the data."
                            },
                            {
                                "role": "user",
                                "content": f"Question: {user_query}\n\nContext:\n{context}"
                            }
                        ],
                        temperature=0.7,
                        max_tokens=500
                    )

                    answer = response["choices"][0]["message"]["content"]
                    st.success("✅ Answer:")
                    st.write(answer)

                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
        else:
            st.warning("⚠️ Please enter a question before submitting.")




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
