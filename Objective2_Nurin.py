import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def app():

    # --------------------------------------------------
    # Page Title
    # --------------------------------------------------
    st.header(
        "Sub-Objective 2: Evaluate the Influence of Scarcity and Serendipity on Shopping Behavior"
    )

    st.subheader("Problem Statement")
    st.write("""
    Scarcity cues such as time-limited promotions and limited product availability, 
    as well as unexpected product discovery, are commonly used in digital commerce. 
    However, without proper analysis, it is difficult to determine how strongly 
    these factors influence students’ shopping perceptions and behaviors.
    """)

    # --------------------------------------------------
    # Load Dataset 
    # --------------------------------------------------
   
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    # ==================================================
    # 1. Correlation Heatmap
    # ==================================================
    correlation_data = df[['Scarcity', 'Serendipity']]
    correlation_matrix = correlation_data.corr()

    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        title="Correlation Heatmap Between Scarcity and Serendipity Scores"
    )

    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation:**  
    - The heatmap shows a moderate positive correlation (r = 0.55) between scarcity and serendipity.
    - Scarcity cues increase product exploration and unexpected discovery.
    - The moderate strength indicates both factors also act independently in influencing shopping behaviour.
    """)

    # ==================================================
    # 2. Monthly Income vs Scores
    # ==================================================
    average_scores_by_income = (
        df.groupby('monthly_income')[['Scarcity', 'Serendipity']]
        .mean()
        .reset_index()
    )

    income_order = ['Under RM100', 'RM100 - RM300', 'Over RM300']
    average_scores_by_income['monthly_income'] = pd.Categorical(
        average_scores_by_income['monthly_income'],
        categories=income_order,
        ordered=True
    )

    melted_scores_income = average_scores_by_income.melt(
        id_vars='monthly_income',
        value_vars=['Scarcity', 'Serendipity'],
        var_name='Score_Type',
        value_name='Average_Score'
    )

    fig = px.bar(
        melted_scores_income,
        x='monthly_income',
        y='Average_Score',
        color='Score_Type',
        barmode='group',
        category_orders={'monthly_income': income_order},
        title="Average Scarcity and Serendipity Scores by Monthly Income",
        labels={
            'monthly_income': 'Monthly Income (RM)',
            'Average_Score': 'Average Score'
        }
    )

    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation:**  
    - Scarcity and serendipity influence shopping behaviour differently across income groups.
    - Students earning under RM100 are more sensitive to scarcity cues.
    - Students in the RM100–RM300 group show the highest serendipity influence, driven by unexpected product discovery.
    """)

    # ==================================================
    # 3. Gender Comparison
    # ==================================================
    average_scores_by_gender = (
        df.groupby('gender')[['Scarcity', 'Serendipity']]
        .mean()
        .reset_index()
    )

    melted_scores_gender = average_scores_by_gender.melt(
        id_vars='gender',
        value_vars=['Scarcity', 'Serendipity'],
        var_name='Score_Type',
        value_name='Average_Score'
    )

    fig = px.bar(
        melted_scores_gender,
        x='gender',
        y='Average_Score',
        color='Score_Type',
        barmode='group',
        title="Average Scarcity and Serendipity Scores by Gender",
        labels={
            'gender': 'Gender',
            'Average_Score': 'Average Score'
        }
    )

    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation:**  
    - Both male and female students are influenced by scarcity and serendipity cues on TikTok Shop.
    - Scarcity scores are similar across genders, indicating equal sensitivity to urgency-based marketing.
    - Male students show slightly higher serendipity scores, suggesting a greater tendency toward exploratory shopping behaviour
    """)

    # ==================================================
    # 4. Box Plots
    # ==================================================
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=[
            "Distribution of Scarcity Scores",
            "Distribution of Serendipity Scores"
        ]
    )

    fig.add_trace(go.Box(y=df['Scarcity'], boxmean=True, name='Scarcity'), row=1, col=1)
    fig.add_trace(go.Box(y=df['Serendipity'], boxmean=True, name='Serendipity'), row=1, col=2)

    fig.update_layout(height=450, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation:**  
    - Box plots indicate that scarcity and serendipity scores are generally moderate to high.
    - Median values fall in the upper-middle range, showing a consistent tendency across respondents.
    - This suggests that students frequently experience urgency and unexpected product discovery when shopping on TikTok Shop.
    """)

    # ==================================================
    # 5. Histograms
    # ==================================================
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=[
            "Distribution of Scarcity Scores",
            "Distribution of Serendipity Scores"
        ]
    )

    fig.add_trace(
        go.Histogram(x=df['Scarcity'], nbinsx=5, histnorm='probability density'),
        row=1, col=1
    )

    fig.add_trace(
        go.Histogram(x=df['Serendipity'], nbinsx=5, histnorm='probability density'),
        row=1, col=2
    )

    fig.update_layout(height=450, showlegend=False, bargap=0.1)
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation:**  
    - Scarcity scores are distributed across the medium to high range.
    - Serendipity scores are skewed toward higher values, indicating stronger influence.
    - This suggests that unexpected product discovery plays a significant role in shaping students’ shopping behaviour on TikTok Shop.
    """)
