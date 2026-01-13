import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def app():
    # ==================================================
    # MAIN TITLE
    # ==================================================
    st.subheader("Students' Impulse Buying Behavior on TikTok Shop")
    
    # Add spacing
    st.markdown("<br><br>", unsafe_allow_html=True)

    # ==================================================
    # SUB-OBJECTIVE & CONTEXT (CENTERED)
    # ==================================================
    st.markdown("""
    <h2 style='text-align: center;'>📌 Sub-Objective 3: Examine Trust, Enjoyment & Shopping Motivation on TikTok Shop</h2>
    <br>
    <h4>🎯 Sub-Objective</h4>
    <p>To investigate the role of trust, enjoyment, and motivation in shaping users’ shopping experiences on TikTok Shop.</p>

    <h4>🧩 Problem Statement</h4>
    <p>Trust and enjoyment are critical psychological factors influencing online shopping decisions. 
    A lack of consumer trust or low enjoyment levels may negatively affect purchasing behavior. 
    Therefore, visually analyzing these constructs can help identify patterns and insights in users’ shopping experiences on TikTok Shop.</p>
    
    <h4>📋 Relevant Questionnaire Sections</h4>
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

    # ==================================================
    # 2️⃣ TRUST BAR CHART
    # ==================================================
    if viz_option == "Trust Bar Chart":
        plot_bar(df, selected_trust_items, "Average Trust Scores")

    # ==================================================
    # 3️⃣ TRUST BOX PLOT
    # ==================================================
    if viz_option == "Trust Box Plot":
        plot_box(df, selected_trust_items, "Trust Item Response Distribution")

    # ==================================================
    # 4️⃣ MOTIVATION BAR CHART
    # ==================================================
    if viz_option == "Motivation Bar Chart":
        plot_bar(df, motivation_items, "Average Motivation Scores")

    # ==================================================
    # 5️⃣ SCATTER PLOT
    # ==================================================
    if viz_option == "Trust vs Motivation Scatter":
        show_trendline = st.checkbox("Show Trend Line", value=True)
        color_col = 'gender' if 'gender' in df.columns else None

        fig = px.scatter(
            df,
            x='Trust_Score',
            y='Motivation_Score',
            color=color_col,
            labels={'Trust_Score': 'Trust Score', 'Motivation_Score': 'Motivation Score'},
            title='Trust vs Motivation'
        )

        if show_trendline:
            x = df['Trust_Score'].values
            y = df['Motivation_Score'].values
            m, b = np.polyfit(x, y, 1)
            x_line = np.linspace(x.min(), x.max(), 100)
            y_line = m * x_line + b
            fig.add_scatter(x=x_line, y=y_line, mode='lines', name='Trend Line')

        st.plotly_chart(fig, use_container_width=True)

    # ==================================================
    # 6️⃣ RADAR CHART - INTERACTIVE
    # ==================================================
    if viz_option == "Trust Radar Chart":
        radar_df = pd.DataFrame({
            'Trust Item': selected_trust_items,
            'Average Score': df[selected_trust_items].mean().values
        })
        radar_df = pd.concat([radar_df, radar_df.iloc[[0]]], ignore_index=True)

        fig_radar = px.line_polar(
            radar_df,
            r='Average Score',
            theta='Trust Item',
            line_close=True,
            markers=True,
            title="Interactive Radar Chart of Trust Dimensions",
            hover_name='Trust Item',
            hover_data={'Average Score': True}
        )
        fig_radar.update_traces(fill='toself')
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(range=[0, 5], visible=True, tickvals=[1,2,3,4,5])
            ),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # Automated key insights
        with st.expander("📌 Key Insights"):
            for i, row in radar_df.iloc[:-1].iterrows():
                score = row['Average Score']
                item = row['Trust Item']
                if score > 4:
                    st.markdown(f"- **{item}** is very high ({score:.2f})")
                elif score < 3:
                    st.markdown(f"- **{item}** is relatively low ({score:.2f})")
                else:
                    st.markdown(f"- **{item}** is moderate ({score:.2f})")
