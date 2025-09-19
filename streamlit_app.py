# app.py
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
import os
from datetime import datetime

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
page = st.sidebar.radio("Go to", ["Home", "Insights", "Dashboard", "About", "Feedback"])

# -----------------------------
# Home
# -----------------------------
if page == "Home":
    st.title("🌍 Global Income Inequality Dashboard")
    st.write("Welcome! This interactive dashboard helps visualize and analyze global income inequality trends.")
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_puciaact.json", height=250)

# -----------------------------
# Insights
# -----------------------------
elif page == "Insights":
    st.header("📈 Key Insights")
    st.markdown("""
    - Inequality varies significantly across regions.  
    - Gini index values highlight disparities in income distribution.  
    - The data helps policymakers, researchers, and students analyze inequality.  
    """)
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json", height=250)

# -----------------------------
# Dashboard
# -----------------------------
elif page == "Dashboard":
    st.header("📊 Dashboard")

    # Loading animation
    with st.spinner("🔍 Analyzing global inequality data..."):
        time.sleep(2)

    # Progress bar simulation
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.success("✅ Analysis Complete")

    # Analysis animation
    lottie_embed("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json", height=250)

    # Example animated metric
    st.subheader("🌍 Global Avg Gini Index")
    components.html(f"""
    <h2 id="num">0</h2>
    <script>
    let start = 0;
    let end = 39;   // Example value
    let duration = 2000;
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
    """, height=60)

# -----------------------------
# About
# -----------------------------
elif page == "About":
    st.header("ℹ️ About This Project")
    st.write("""
    This dashboard was built to provide insights into global income inequality using interactive data visualization.  
    It integrates datasets, metrics, and animations to make the analysis more engaging.  

    **Tech Stack**:  
    - Python  
    - Streamlit  
    - Pandas  
    - HTML + Lottie animations
    """)
    lottie_embed("https://assets2.lottiefiles.com/packages/lf20_puciaact.json", height=200)

# -----------------------------
# Feedback
# -----------------------------
elif page == "Feedback":
    st.header("💬 Feedback")

    feedback = st.text_area("Share your thoughts about this dashboard:")
    if st.button("Submit Feedback"):
        st.success("🎉 Thank you for your valuable feedback!")
        lottie_embed("https://assets2.lottiefiles.com/packages/lf20_puciaact.json", height=200)
