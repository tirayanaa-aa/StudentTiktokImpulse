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
    # 1. Scatter Plot
    # ==================================================
    st.subheader("Scarcity vs Serendipity Quadrant Analysis")
    x_col = 'Scarcity'
    y_col = 'Serendipity'
    color_col = 'impulse_purchase'
    
    mean_x = df[x_col].mean()
    mean_y = df[y_col].mean()
    
    fig = px.scatter(
    df,
    x=x_col,
    y=y_col,
    color=color_col,
    color_continuous_scale='Viridis',
    opacity=0.7,
    title="Scarcity vs Serendipity with Impulse Purchase Quadrants"
    )
    
    fig.add_vline(
    x=mean_x,
    line_dash="dash",
    line_color="gray",
    annotation_text=f"Mean Scarcity ({mean_x:.2f})",
    annotation_position="top"
    )
    
    fig.add_hline(
    y=mean_y,
    line_dash="dash",
    line_color="gray",
    annotation_text=f"Mean Serendipity ({mean_y:.2f})",
    annotation_position="right"
    )
    
    fig.update_layout(
    height=500,
    xaxis_title="Scarcity Score",
    yaxis_title="Serendipity Score",
    template="plotly_white"
    
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    **Interpretation:**  
    - The dashed vertical and horizontal lines represent the mean scarcity (3.68) and mean serendipity (3.85) values, dividing the data into four behavioral quadrants.
    - Impulse buying behavior is strongest when both scarcity and serendipity are high.
    - Both factors individually influence impulse buying, but their combined effect is significantly stronger.
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
