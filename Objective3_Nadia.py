import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.subheader("Students' Impulse Buying Behavior on TikTok Shop")

    # ==================================================
    # SUB-OBJECTIVE & CONTEXT
    # ==================================================
    st.markdown("""
    ## 📌 Sub-Objective 3: Examine Trust, Enjoyment & Shopping Motivation on TikTok Shop

    ### 🎯 Sub-Objective
    To investigate the role of trust, enjoyment, and motivation in shaping users’ shopping experiences on TikTok Shop.

    ### 🧩 Problem Statement
    Trust and enjoyment are critical psychological factors influencing online shopping decisions. 
    A lack of consumer trust or low enjoyment levels may negatively affect purchasing behavior. 
    Therefore, visually analyzing these constructs can help identify patterns and insights in users’ shopping experiences on TikTok Shop.
    
    ### 📋 Relevant Questionnaire Sections
    - **Section 5:** Trust in TikTok Shop (TR)  
    - **Section 6:** Fun and Motivation in Shopping (HM)
    """)

    # ==================================================
    # LOAD DATASET
    # ==================================================
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    # ==================================================
    # SIDEBAR FILTERS
    # ==================================================
    st.sidebar.header("🔍 Data Filters")
    if 'gender' in df.columns:
        selected_gender = st.sidebar.multiselect(
            "Select Gender",
            options=df['gender'].unique(),
            default=df['gender'].unique()
        )
        df = df[df['gender'].isin(selected_gender)]

    if 'age_group' in df.columns:
        selected_age = st.sidebar.multiselect(
            "Select Age Group",
            options=df['age_group'].unique(),
            default=df['age_group'].unique()
        )
        df = df[df['age_group'].isin(selected_age)]

    # ==================================================
    # DEFINE FACTORS GROUPS
    # ==================================================
    trust_items = [
        'trust_no_risk',
        'trust_reliable',
        'trust_variety_meets_needs',
        'trust_sells_honestly',
        'trust_quality_matches_description'
    ]

    motivation_items = [
        'relax_reduce_stress',
        'motivated_by_discount_promo',
        'motivated_by_gifts'
    ]

    # ==================================================
    # CREATE COMPOSITE SCORES
    # ==================================================
    df['Trust_Score'] = df[trust_items].mean(axis=1)
    df['Motivation_Score'] = df[motivation_items].mean(axis=1)
    df = df.dropna(subset=['Trust_Score', 'Motivation_Score'])

    # ==================================================
    # SUMMARY METRICS
    # ==================================================
    st.markdown("## 📊 Summary Metrics")
    metric_cols = ['Trust_Score', 'Motivation_Score']
    missing_cols = [c for c in metric_cols if c not in df.columns]

    if not missing_cols:
        col1, col2 = st.columns(2)
        col1.metric(
            label="Average Trust Score",
            value=f"{df['Trust_Score'].mean():.2f}",
            delta=f"{df['Trust_Score'].max() - df['Trust_Score'].min():.2f} range"
        )
        col2.metric(
            label="Average Motivation Score",
            value=f"{df['Motivation_Score'].mean():.2f}",
            delta=f"{df['Motivation_Score'].max() - df['Motivation_Score'].min():.2f} range"
        )

        summary_df = df[metric_cols].describe().round(2)
        styled_df = summary_df.style.background_gradient(cmap='Blues', axis=1)
        st.dataframe(styled_df, height=220)
    else:
        st.warning(f"Missing columns for summary metrics: {missing_cols}")

    # ==================================================
    # VISUALIZATION SELECTOR
    # ==================================================
    st.markdown("## 📊 Select Visualization Type")
    viz_option = st.selectbox(
        "Choose a visualization:",
        [
            "Correlation Heatmap",
            "Trust Bar Chart",
            "Trust Box Plot",
            "Motivation Bar Chart",
            "Trust vs Motivation Scatter",
            "Trust Radar Chart"
        ]
    )

    # ==================================================
    # 1️⃣ CORRELATION HEATMAP
    # ==================================================
    if viz_option == "Correlation Heatmap":
        corr_items = trust_items + motivation_items
        missing_corr = [c for c in corr_items if c not in df.columns]

        if not missing_corr:
            corr = df[corr_items].corr()
            fig1 = px.imshow(
                corr,
                text_auto='.2f',
                zmin=-1,
                zmax=1,
                color_continuous_scale='RdBu',
                title='Correlation Matrix of Trust & Motivation Items'
            )
            st.plotly_chart(fig1, use_container_width=True)

            with st.expander("📌 Key Insights"):
                st.markdown("""
                - Trust-related items show strong internal consistency.
                - Promotional incentives are strongly associated with motivation.
                - Trust supports motivation rather than directly driving impulse buying.
                """)
        else:
            st.warning(f"Missing columns for correlation: {missing_corr}")

    # ==================================================
    # 2️⃣ TRUST BAR CHART
    # ==================================================
    if viz_option == "Trust Bar Chart":
        st.markdown("### 🎛 Select Trust Dimensions")
        selected_trust_items = st.multiselect(
            "Choose trust items to analyze:",
            options=trust_items,
            default=trust_items
        )
        if not selected_trust_items:
            st.warning("Please select at least one trust item.")
            selected_trust_items = trust_items

        trust_means = df[selected_trust_items].mean().reset_index()
        trust_means.columns = ['Trust Item', 'Mean Score']

        fig2 = px.bar(
            trust_means,
            x='Trust Item',
            y='Mean Score',
            title="Average Trust Scores"
        )
        st.plotly_chart(fig2, use_container_width=True)

        with st.expander("📌 Key Insights"):
            st.markdown("""
            - Overall, trust levels are positive.
            - Product variety and quality are the strongest areas.
            - Honesty and reliability are solid.
            - "No risk" is slightly lower, suggesting room for improvement.
            """)

    # ==================================================
    # 3️⃣ TRUST BOX PLOT
    # ==================================================
    if viz_option == "Trust Box Plot":
        trust_long = df[trust_items].melt(var_name='Trust Item', value_name='Response')
        fig3 = px.box(trust_long, x='Trust Item', y='Response', points='all', title='Trust Item Response Distribution')
        st.plotly_chart(fig3, use_container_width=True)

        with st.expander("📌 Key Insights"):
            st.markdown("""
            - Most trust items have median responses between 3 and 4.
            - Product variety shows higher median and wider spread.
            - Seller honesty and product description accuracy are consistent.
            """)

    # ==================================================
    # 4️⃣ MOTIVATION BAR CHART
    # ==================================================
    if viz_option == "Motivation Bar Chart":
        mot_means = df[motivation_items].mean().reset_index()
        mot_means.columns = ['Motivation Item', 'Mean Score']
        fig4 = px.bar(mot_means, x='Motivation Item', y='Mean Score', title="Average Motivation Scores")
        st.plotly_chart(fig4, use_container_width=True)

        with st.expander("📌 Key Insights"):
            st.markdown("""
            - Discounts and promotions are the strongest motivators.
            - Gifts also play a meaningful role.
            - Relaxation and stress reduction show moderate motivation.
            """)

    # ==================================================
    # 5️⃣ SCATTER PLOT
    # ==================================================
    if viz_option == "Trust vs Motivation Scatter":
        show_trendline = st.checkbox("Show Trend Line", value=True)

        fig5 = px.scatter(
            df,
            x='Trust_Score',
            y='Motivation_Score',
            labels={'Trust_Score': 'Trust Score', 'Motivation_Score': 'Motivation Score'},
            title='Trust vs Motivation'
        )

        if show_trendline:
            x = df['Trust_Score'].values
            y = df['Motivation_Score'].values
            m, b = np.polyfit(x, y, 1)
            x_line = np.linspace(x.min(), x.max(), 100)
            y_line = m * x_line + b
            fig5.add_scatter(x=x_line, y=y_line, mode='lines', name='Trend Line')

        st.plotly_chart(fig5, use_container_width=True)

        with st.expander("📌 Key Insights"):
            st.markdown("""
            - Positive relationship between trust and motivation.
            - Higher trust is associated with higher motivation.
            - Trend line shows steady increase.
            """)

    # ==================================================
    # 6️⃣ RADAR CHART
    # ==================================================
    if viz_option == "Trust Radar Chart":
        labels = trust_items
        values = df[selected_trust_items].mean().tolist()
        values += values[:1]  # complete loop
        angles = np.linspace(0, 2 * np.pi, len(labels)+1)

        fig6, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
        ax.plot(angles, values, linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles[:-1] * 180/np.pi, labels)
        st.pyplot(fig6)

        with st.expander("📌 Key Insights"):
            st.markdown("""
            - Trust is strong across all dimensions.
            - Product variety and quality are highest.
            - Honesty and reliability are positive.
            - "No risk" is slightly lower, indicating room for reassurance.
            """)
