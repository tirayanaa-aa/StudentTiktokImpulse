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

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    # --------------------------------------------------
    # Define factor groups
    # --------------------------------------------------
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

    # --------------------------------------------------
    # Create composite scores
    # --------------------------------------------------
    df['Trust_Score'] = df[trust_items].mean(axis=1)
    df['Motivation_Score'] = df[motivation_items].mean(axis=1)

     # 🔧 SAFETY: remove missing values (important)
    df = df.dropna(subset=['Trust_Score', 'Motivation_Score'])

    # --------------------------------------------------
    # Summary Metrics
    # --------------------------------------------------
    st.markdown("## 📊 Summary Metrics")
    metric_cols = ['Trust_Score', 'Motivation_Score']
    missing_cols = [c for c in metric_cols if c not in df.columns]

    if not missing_cols:
        col1, col2 = st.columns(2)
        col1.metric("Average Trust Score", round(df['Trust_Score'].mean(), 2))
        col2.metric("Average Motivation Score", round(df['Motivation_Score'].mean(), 2))

        st.markdown("### 🔍 Descriptive Statistics")
        st.dataframe(df[metric_cols].describe().round(2))
    else:
        st.warning(f"Missing columns for summary metrics: {missing_cols}")


    # --------------------------------------------------
    # 1️⃣ Correlation Heatmap
    # --------------------------------------------------
    st.markdown("### 1️⃣ Correlation Between Trust & Motivation Items")
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
    else:
        st.warning(f"Missing columns for correlation: {missing_corr}")

        st.write("""
        **Interpretation:**  
        The correlation heatmap supports the finding that trust-related factors such as reliability, honesty, and product quality are positively associated with motivation factors such as discounts and gifts.
        This indicates that higher trust increases shopping motivation on TikTok Shop.
        """)

    # --------------------------------------------------
    # 2️⃣ Bar Chart – Trust Items
    # --------------------------------------------------
    st.markdown("### 2️⃣ Average Trust Scores by Item")
    missing_trust = [c for c in trust_items if c not in df.columns]
    if not missing_trust:
        trust_means = df[trust_items].mean().reset_index()
        trust_means.columns = ['Trust Item', 'Mean Score']
        fig2 = px.bar(trust_means, x='Trust Item', y='Mean Score', title="Average Trust Scores")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning(f"Missing trust columns: {missing_trust}")
        
        st.write("""
        **Interpretation:**  
        This bar chart compares the average trust scores across different trust dimensions.
        The results show that product variety and reliability receive the highest trust ratings,
        indicating these aspects are most important to respondents.
        """)
        
    # --------------------------------------------------
    # 3️⃣ Box Plot – Trust Responses
    # --------------------------------------------------
    st.markdown("### 3️⃣ Distribution of Trust Responses")
    if not missing_trust:
        trust_long = df[trust_items].melt(var_name='Trust Item', value_name='Response')
        fig3 = px.box(trust_long, x='Trust Item', y='Response', points='all', title='Trust Item Response Distribution')
        st.plotly_chart(fig3, use_container_width=True)

        st.write("""
        **Interpretation:**  
        The box plot shows variation in trust responses across different trust items.
        Some items have wider ranges, indicating mixed opinions, while others show more consistent responses. 
        This visualization highlights variability, medians, and outliers that cannot be observed using mean values alone.
        """)

    # --------------------------------------------------
    # 4️⃣ Bar Chart – Motivation Items
    # --------------------------------------------------
    st.markdown("### 4️⃣ Average Motivation Scores by Item")
    missing_mot = [c for c in motivation_items if c not in df.columns]
    if not missing_mot:
        mot_means = df[motivation_items].mean().reset_index()
        mot_means.columns = ['Motivation Item', 'Mean Score']
        fig4 = px.bar(mot_means, x='Motivation Item', y='Mean Score', title="Average Motivation Scores")
        st.plotly_chart(fig4, use_container_width=True)

        st.write("""
        **Interpretation:**  
        Discounts and promotions emerge as the strongest motivational factor, followed by gifts and stress reduction. 
        This indicates that promotional strategies are highly effective in motivating impulse purchases.
        """)

    # --------------------------------------------------
    # 5️⃣ Scatter Plot – Trust vs Motivation (with trendline)
    # --------------------------------------------------
    st.markdown("### 5️⃣ Relationship Between Trust and Motivation")
    if 'Trust_Score' in df.columns and 'Motivation_Score' in df.columns:
        fig5 = px.scatter(
            df,
            x='Trust_Score',
            y='Motivation_Score',
            labels={'Trust_Score': 'Trust Score', 'Motivation_Score': 'Motivation Score'},
            title='Trust vs Motivation'
        )

        # Add manual trendline
        x = df['Trust_Score'].values
        y = df['Motivation_Score'].values
        m, b = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = m * x_line + b
        fig5.add_scatter(x=x_line, y=y_line, mode='lines', name='Trend Line', line=dict(width=3))
        st.plotly_chart(fig5, use_container_width=True)

        st.write("""
        **Interpretation:**  
        The scatter plot shows a positive relationship between trust and shopping motivation.
        As trust increases, motivation also increases, supporting the importance of trust
        as a psychological driver of impulse buying behavior.
        """)

    
    # --------------------------------------------------
    # 6️⃣ Radar Chart – Trust Dimensions
    # --------------------------------------------------
    st.markdown("### 6️⃣ Trust Dimension Radar Chart")
    if not missing_trust:
        import matplotlib.pyplot as plt
        labels = trust_items
        values = trust_means['Mean Score'].tolist()
        values += values[:1]  # complete loop
        angles = np.linspace(0, 2 * np.pi, len(labels)+1)
        fig6, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
        ax.plot(angles, values, linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles[:-1] * 180/np.pi, labels)
        st.pyplot(fig6)

        st.write("""
        **Interpretation:**  
        The radar chart shows that trust dimensions are relatively balanced, with slightly higher scores for reliability and product quality, highlighting their importance in shaping overall trust.
        """)
