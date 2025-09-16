import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")
st.title("🌍 Global Income Inequality Dashboard")

# Power BI iframe URL (from your earlier code)
pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYjM4NjU1MGItYzM2Yi00YjAxLWIzYTYtNjgyMWRkMTNiNDhkIiwidCI6IjZmNzAzYzQwLWE4MTEtNDUwYS1iZmFmLWNmM2QxZTczM2RhZiJ9"

# Method 1: Simple iframe
components.iframe(pbi_url, height=800)

# Method 2: Full HTML (if you want fullscreen option enabled)
html_code = f"""
<iframe title="Global Income Inequality Dashboard" width="100%" height="800"
        src="{pbi_url}" frameborder="0" allowFullScreen="true"></iframe>
"""
components.html(html_code, height=820, scrolling=True)
