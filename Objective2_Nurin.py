import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def app():
    st.header(
    "Sub-Objective 2: Evaluate the Influence of Scarcity and Serendipity on Shopping Behavior"
    )
    st.subheader("Problem Statement")
    st.write("""
    Scarcity cues such as time-limited promotions and limited product availability, as well as unexpected product discovery, are commonly used in digital commerce.
    However, without proper analysis, it is difficult to determine how strongly these factors influence student’s shopping perceptions and behaviors.
    """)
  
#-----------------------------------------------
# Load dataset
#-----------------------------------------------
df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")


#Heatmap
# Create a sub-dataframe with only 'Scarcity' and 'Serendipity'
correlation_data = df[['Scarcity', 'Serendipity']]

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Create Plotly heatmap
fig = px.imshow(
    correlation_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu",
    zmin=-1,
    zmax=1
)

fig.update_layout(
    title="Correlation Heatmap Between Scarcity and Serendipity Scores",
    width=500,
    height=450
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
st.write("""
    **Interpretation:**  
    The correlation heatmap shows a moderate positive relationship, at 0.55, between Scarcity and Serendipity.Scarcity makes students feel there is urgency to go out and find products, which in return makes them discover new or unplanned items.
    However, the strength of the relationship is not that high, meaning both Scarcity and Serendipity still affect shopping behavior differently.
    """)

#Monthly Income Bar Chart
# Calculate the average Scarcity and Serendipity scores by monthly_income
average_scores_by_income = (
    df.groupby('monthly_income')[['Scarcity', 'Serendipity']]
    .mean()
    .reset_index()
)

# Define income order
income_order = ['Under RM100', 'RM100 - RM300', 'Over RM300']
average_scores_by_income['monthly_income'] = pd.Categorical(
    average_scores_by_income['monthly_income'],
    categories=income_order,
    ordered=True
)
average_scores_by_income = average_scores_by_income.sort_values('monthly_income')

# Melt dataframe for Plotly
melted_scores_income = average_scores_by_income.melt(
    id_vars='monthly_income',
    value_vars=['Scarcity', 'Serendipity'],
    var_name='Score_Type',
    value_name='Average_Score'
)

# Create Plotly grouped bar chart
fig = px.bar(
    melted_scores_income,
    x='monthly_income',
    y='Average_Score',
    color='Score_Type',
    barmode='group',
    category_orders={'monthly_income': income_order},
    labels={
        'monthly_income': 'Monthly Income (in RM)',
        'Average_Score': 'Average Score',
        'Score_Type': 'Score Type'
    },
    title='Average Scarcity and Serendipity Scores by Monthly Income'
)

fig.update_layout(
    height=500,
    xaxis_tickangle=-45
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
st.write("""
    **Interpretation:**  
   Results show that scarcity and Serendipity discovery both influence shopping behaviour on TikTok Shop, with differences across income groups.
   Students earning less than RM100 are strongly influenced by limited-time offers and low product availability.The highest unexpected discovery score is recorded in the RM100–RM300 group, which suggests that this group is most influenced by the discovery of new or unexpected products
    """)

#Gender Bar Chart
# Calculate the average Scarcity and Serendipity scores by gender
average_scores_by_gender = (
    df.groupby('gender')[['Scarcity', 'Serendipity']]
    .mean()
    .reset_index()
)

# Melt dataframe for Plotly
melted_scores = average_scores_by_gender.melt(
    id_vars='gender',
    value_vars=['Scarcity', 'Serendipity'],
    var_name='Score_Type',
    value_name='Average_Score'
)

# Create Plotly grouped bar chart
fig = px.bar(
    melted_scores,
    x='gender',
    y='Average_Score',
    color='Score_Type',
    barmode='group',
    labels={
        'gender': 'Gender',
        'Average_Score': 'Average Score',
        'Score_Type': 'Score Type'
    },
    title='Average Scarcity and Serendipity Scores by Gender'
)

fig.update_layout(
    height=450,
    xaxis_tickangle=0
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
st.write("""
    **Interpretation:**  
    From the results, it can be noted that both male and female shoppers are driven by scarcity and serendipity in TikTok Shop.
    Scarcity scores of both male and female shoppers are more or less at par as both male and female shoppers are equally impacted by scarcity marketing. Males are slightly more driven by serendipity as their serendipity score is a bit higher compared to females.
    """)

#Box Plot
# Create subplots (1 row, 2 columns)
fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=[
        "Distribution of Scarcity Score",
        "Distribution of Serendipity Score"
    ]
)

# Box plot for Scarcity
fig.add_trace(
    go.Box(
        y=df['Scarcity'],
        name='Scarcity',
        boxmean=True
    ),
    row=1,
    col=1
)

# Box plot for Serendipity
fig.add_trace(
    go.Box(
        y=df['Serendipity'],
        name='Serendipity',
        boxmean=True
    ),
    row=1,
    col=2
)

# Layout adjustments
fig.update_layout(
    height=450,
    showlegend=False
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
st.write("""
    **Interpretation:**  
    The box plots above demonstrate that Scarcity and Serendipity scores tend to be moderately to highly valued among consumers on TikTok Shop.
    The median scores for Scarcity and Serendipity are close to the upper-middle levels, suggesting that consumers tend to be exposed to feelings of scarcity and serendipity during their shopping experiences on TikTok Shop.
    """)

#Histogram
# Create subplots (1 row, 2 columns)
fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=[
        "Distribution of Scarcity Score",
        "Distribution of Serendipity Score"
    ]
)

# Histogram for Scarcity Score
fig.add_trace(
    go.Histogram(
        x=df['Scarcity'],
        nbinsx=5,
        histnorm='probability density',
        name='Scarcity'
    ),
    row=1,
    col=1
)

# Histogram for Serendipity Score
fig.add_trace(
    go.Histogram(
        x=df['Serendipity'],
        nbinsx=5,
        histnorm='probability density',
        name='Serendipity'
    ),
    row=1,
    col=2
)

# Layout adjustments
fig.update_layout(
    height=450,
    showlegend=False,
    bargap=0.1
)

# Axis labels
fig.update_xaxes(title_text="Scarcity Score", row=1, col=1)
fig.update_yaxes(title_text="Density", row=1, col=1)

fig.update_xaxes(title_text="Serendipity Score", row=1, col=2)
fig.update_yaxes(title_text="Density", row=1, col=2)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
st.write("""
    **Interpretation:**  
    The distribution of data reveals that both scarcity and serendipity have a significant impact on purchasing habits when it comes to shopping on TikTok Shop.
    The scarcity scores vary across the medium to high range. Additionally, the scores on serendipity lie on the higher side, implying consumers are often driven by discovering products that were unknown to them.
    """)
