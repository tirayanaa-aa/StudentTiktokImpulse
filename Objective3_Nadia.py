import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def app():
    # ==================================================
    # MAIN TITLE (BIG & CENTERED)
    # ==================================================
    st.markdown("""
    <h1 style='text-align: center; font-size: 36px; color: #1f77b4;'>
        Students' Impulse Buying Behavior on TikTok Shop
    </h1>
    <br><br>
    """, unsafe_allow_html=True)

    # ==================================================
    # CONTEXT / PROBLEM STATEMENT (CENTERED OPTIONAL)
    # ==================================================
    st.markdown("""
    <h4 style='text-align: left;'>🎯 Objective</h4>
    <p>To investigate the role of trust, enjoyment, and motivation in shaping users’ shopping experiences on TikTok Shop.</p>

    <h4 style='text-align: left;'>🧩 Problem Statement</h4>
    <p>Trust and enjoyment are critical psychological factors influencing online shopping decisions. 
    A lack of consumer trust or low enjoyment levels may negatively affect purchasing behavior. 
    Therefore, visually analyzing these constructs can help identify patterns and insights in users’ shopping experiences on TikTok Shop.</p>
    
    <h4 style='text-align: left;'>📋 Relevant Questionnaire Sections</h4>
    <ul>
        <li><b>Section 5:</b> Trust in TikTok Shop (TR)</li>
        <li><b>Section 6:</b> Fun and Motivation in Shopping (HM)</li>
    </ul>
    """, unsafe_allow_html=True)
    
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
    # CENTRALIZED TRUST ITEM SELECTION
    # ==================================================
    st.sidebar.header("🎛 Select Trust Items for Analysis")
    selected_trust_items = st.sidebar.multiselect(
        "Choose trust items:",
        options=trust_items,
        default=trust_items
    )
    if not selected_trust_items:
        st.warning("Please select at least one trust item.")
        selected_trust_items = trust_items

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

        summary_df = df[metric_cols].agg(['mean','min','max']).T.round(2)
        st.dataframe(summary_df.style.background_gradient(cmap='Blues'), height=220)
    else:
        st.warning(f"Missing columns for summary metrics: {missing_cols}")

    # ==================================================
    # HELPER FUNCTIONS
    # ==================================================
    def plot_bar(df, items, title):
        means = df[items].mean().reset_index()
        means.columns = ['Item', 'Mean Score']
        fig = px.bar(means, x='Item', y='Mean Score', title=title)
        st.plotly_chart(fig, use_container_width=True)
        # Automated insights
        with st.expander("📌 Key Insights"):
            for i, row in means.iterrows():
                if row['Mean Score'] > 4:
                    st.markdown(f"- **{row['Item']}** is very high ({row['Mean Score']:.2f})")
                elif row['Mean Score'] < 3:
                    st.markdown(f"- **{row['Item']}** is relatively low ({row['Mean Score']:.2f})")
                else:
                    st.markdown(f"- **{row['Item']}** is moderate ({row['Mean Score']:.2f})")

    def plot_box(df, items, title):
        df_long = df[items].melt(var_name='Item', value_name='Score')
        fig = px.box(df_long, x='Item', y='Score', points='all', title=title)
        st.plotly_chart(fig, use_container_width=True)

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
            fig = px.imshow(
                corr,
                text_auto='.2f',
                zmin=-1,
                zmax=1,
                color_continuous_scale='RdBu',
                title='Correlation Matrix of Trust & Motivation Items'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Highlight strong correlations
            strong_corr = corr[(corr.abs() > 0.7) & (corr.abs() < 1)]
            if not strong_corr.empty:
                st.markdown("**Strong correlations (>|0.7|):**")
                st.dataframe(strong_corr)


            # -------------------------
            # INTERPRETATION / INSIGHTS
            # -------------------------
            with st.expander("📌 Key Insights - Correlation Heatmap"):
                st.markdown("""
                <ul style="margin-left:15px;">
                    <li>Trust-related items show moderate to strong positive correlations among themselves, particularly between honesty and quality matching the product description.</li>
                    <li>Motivation factors such as discounts and gifts are also strongly correlated, showing consistent promotional influence.</li>
                    <li>Some trust items show moderate positive relationships with motivation variables, suggesting that higher trust is associated with increased shopping motivation.</li>
                    <li>Correlations between trust and motivation are generally weaker than within each construct, indicating that trust supports motivation rather than directly driving it.</li>
                </ul>
                """, unsafe_allow_html=True)

    
    # ==================================================
    # 2️⃣ BAR CHART - TRUST ITEMS
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
    
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        with st.expander("📌 Key Insights - Trust Bar Chart"):
            st.markdown("""
            <ul style="margin-left:15px;">
                <li>Overall, trust levels are positive, with all items scoring above the midpoint, indicating customers generally feel confident about the brand.</li>
                <li>Product variety is the strongest area, suggesting the offerings align well with customer expectations.</li>
                <li>Trust in reliability, honesty, and quality matching the description is also solid, reflecting consistent experiences.</li>
                <li>The slightly lower score for "no risk" suggests some minor concerns that could be addressed through clearer guarantees or communication.</li>
            </ul>
            """, unsafe_allow_html=True)

    # ==================================================
    # 3️⃣ BOX PLOT - TRUST RESPONSES
    # ==================================================
    if viz_option == "Trust Box Plot":
        trust_long = df[trust_items].melt(var_name='Trust Item', value_name='Response')
        fig3 = px.box(trust_long, x='Trust Item', y='Response', points='all', title='Trust Item Response Distribution')
        st.plotly_chart(fig3, use_container_width=True)
    
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        with st.expander("📌 Key Insights - Trust Box Plot"):
            st.markdown("""
            <ul style="margin-left:15px;">
                <li>Most trust items have median responses between 3 and 4, indicating overall positive trust among respondents.</li>
                <li>Product variety shows a slightly higher median and wider spread, suggesting generally favorable perceptions.</li>
                <li>Trust in honesty and accuracy is relatively consistent, with fewer extreme values.</li>
                <li>Respondents tend to agree with trust statements, although variation exists across different dimensions.</li>
            </ul>
            """, unsafe_allow_html=True)

    # ==================================================
    # 4️⃣ BAR CHART - MOTIVATION ITEMS
    # ==================================================
    if viz_option == "Motivation Bar Chart":
        mot_means = df[motivation_items].mean().reset_index()
        mot_means.columns = ['Motivation Item', 'Mean Score']
        fig4 = px.bar(mot_means, x='Motivation Item', y='Mean Score', title="Average Motivation Scores")
        st.plotly_chart(fig4, use_container_width=True)
    
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        with st.expander("📌 Key Insights - Motivation Bar Chart"):
            st.markdown("""
            <ul style="margin-left:15px;">
                <li>Discounts and promotions are the strongest motivator, standing out as the main driver of customer interest.</li>
                <li>Gifts also play a meaningful role, showing that added value beyond the core product resonates with customers.</li>
                <li>Relaxation and stress reduction score slightly lower, indicating moderate motivation rather than disinterest.</li>
                <li>Customers appear more motivated by tangible incentives than emotional or lifestyle benefits.</li>
            </ul>
            """, unsafe_allow_html=True)

    # ==================================================
    # 5️⃣ SCATTER PLOT -TRUST vs MOTIVATION
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
    
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        with st.expander("📌 Key Insights - Trust vs Motivation Scatter"):
            st.markdown("""
            <ul style="margin-left:15px;">
                <li>The scatter plot shows a positive relationship between trust and motivation; higher trust generally corresponds to higher motivation.</li>
                <li>The upward trend line indicates motivation increases steadily as trust improves.</li>
                <li>Some variation exists at similar trust levels, but the overall pattern is consistent.</li>
                <li>This suggests that trust plays a supportive role in enhancing consumer motivation on TikTok Shop.</li>
            </ul>
            """, unsafe_allow_html=True)

    # ==================================================
    # 6️⃣ RADAR CHART - INTERACTIVE
    # ==================================================
    if viz_option == "Trust Radar Chart":
        labels = selected_trust_items
        values = df[selected_trust_items].mean().tolist()
        values += values[:1]  # close the loop
    
        fig6 = go.Figure(
            data=go.Scatterpolar(
                r=values,
                theta=labels + [labels[0]],  # complete loop for radar
                fill='toself',
                name='Trust Levels',
                line=dict(color='blue')
            )
        )
    
        fig6.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0,5])
            ),
            showlegend=False,
            title="Trust Radar Chart"
        )
    
        st.plotly_chart(fig6, use_container_width=True)
    
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        with st.expander("📌 Key Insights - Trust Radar Chart"):
            st.markdown("""
            <ul style="margin-left:15px;">
                <li>Overall, trust levels are strong across all dimensions, with no area showing serious weakness.</li>
                <li>Customers feel most confident that product variety meets their needs and quality matches the description, showing expectations are largely met.</li>
                <li>Trust in honesty and reliability is high, reflecting positive perceptions of seller integrity.</li>
                <li>The slightly lower score on "no risk" suggests some customers may still feel cautious, leaving room to strengthen reassurance and transparency.</li>
            </ul>
            """, unsafe_allow_html=True)
