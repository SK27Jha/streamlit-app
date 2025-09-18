elif page == "🔎 Insight":
    st.markdown("## 🔎 Insights")

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

    # Allow user to upload CSV
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df_insight = pd.read_csv(uploaded_file)
        st.dataframe(df_insight, use_container_width=True)

        # Basic numeric metrics
        st.markdown("---")
        st.write("### 📈 Summary Metrics")
        for col in df_insight.select_dtypes(include=['int64', 'float64']).columns:
            st.metric(f"{col} Average", f"{df_insight[col].mean():.2f}")
    else:
        st.info("⚠️ Please upload your CSV file to view dataset insights.")

    st.markdown('</div>', unsafe_allow_html=True)
