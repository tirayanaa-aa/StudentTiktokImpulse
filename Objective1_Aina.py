import plotly.express as px
import streamlit as st
import pandas as pd


st.set_page_config(page_title="TikTok Shop Analysis", layout="wide")


def app():
    # --- Page Header ---
    st.header("Sub-Objective 1: Analyze the Demographic Profile and TikTok Shop Usage")
    
    # --- Problem Statement Section ---
    st.subheader("Problem Statement")
    st.info("""
    E-commerce platforms like TikTok Shop serve users from diverse demographic backgrounds. 
    However, limited understanding of how factors such as gender, age group, faculty, 
    and income relate to TikTok Shop usage may reduce the effectiveness of targeted 
    marketing strategies and user experience optimization.
    """)

    # --- Load Dataset ---
    # Ensuring the dataframe is loaded within the page function
    try:
        df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")
        

# 1. Prepare the data
# Plotly works best with a DataFrame where columns are clearly named
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']

# 2. Create the Plotly figure
fig = px.pie(
    gender_counts, 
    values='count', 
    names='gender', 
    title='Distribution of Gender',
    color_discrete_sequence=px.colors.qualitative.Pastel, # Matches your 'pastel' palette
    hole=0 # Set to 0.4 if you prefer a donut chart style
)

# 3. Display in Streamlit
# use_container_width=True ensures the chart scales with the Streamlit layout
st.plotly_chart(fig, use_container_width=True)



# 1. Define the correct order
age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']

# 2. Create the Plotly chart
# px.histogram automatically performs the "count" aggregation
fig = px.histogram(
    df, 
    x='age', 
    color='tiktok_shop_experience',
    barmode='group',                 # Side-by-side bars (like Seaborn)
    category_orders={'age': age_order}, # Ensures the age groups follow your specific order
    color_discrete_sequence=px.colors.sequential.Viridis,
    title='TikTok Shop Usage across Age Groups',
    labels={
        'age': 'Age Group', 
        'tiktok_shop_experience': 'Experience',
        'count': 'Number of Users'
    }
)

# 3. Refine the layout
fig.update_layout(
    yaxis_title="Count",
    xaxis_title="Age Group",
    legend_title="TikTok Shop Experience"
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)










# 1. Prepare the data
gender_counts = df['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']

# 2. Create the Plotly figure
fig = px.pie(
    gender_counts, 
    values='count', 
    names='gender', 
    title='Distribution of Gender',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0 # Set to 0.4 for a donut chart!
)

# 3. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


# 1. Prepare the data
# We reset the index to turn the Series into a DataFrame that Plotly can read easily
faculty_counts = df['faculty'].value_counts().reset_index()
faculty_counts.columns = ['faculty', 'count']

# 2. Sort the data (matching your ascending=True logic)
faculty_counts = faculty_counts.sort_values(by='count', ascending=True)

# 3. Create the Plotly Bar Chart
fig = px.bar(
    faculty_counts, 
    x='count', 
    y='faculty', 
    orientation='h',
    title='Distribution of Faculty',
    color='count',                # Optional: Adds a color gradient based on value
    color_continuous_scale='Viridis', # Matches your 'viridis' palette
    labels={'count': 'Count', 'faculty': 'Faculty'}
)

# Optional: Improve layout (removes legend for the color scale if not needed)
fig.update_layout(showlegend=False, coloraxis_showscale=False)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


# 1. Create the crosstab (same as your original code)
data_crosstab = pd.crosstab(df['monthly_income'], df['BrandDesign'])

# 2. Create the Heatmap using Plotly Express
fig = px.imshow(
    data_crosstab,
    text_auto=True,                # This replaces annot=True and fmt='d'
    color_continuous_scale='Viridis', 
    aspect='auto',                 # Adjusts cell sizing to fit the container
    labels=dict(
        x='Brand Design Score', 
        y='Monthly Income Group', 
        color='Count'              # Label for the color bar
    ),
    title='Distribution of Brand Design Preference by Income Level'
)

# 3. Optional: Move the x-axis labels to the bottom (Plotly defaults to top for heatmaps)
fig.update_xaxes(side="bottom")

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


# 1. Create the crosstab and reset index 
# Plotly Express works best when variables are columns, not just indices
crosstab_df = pd.crosstab(df['gender'], df['tiktok_shop_experience']).reset_index()

# 2. Create the Stacked Bar Chart
# barmode='stack' is the default for px.bar, but we'll be explicit
fig = px.bar(
    crosstab_df, 
    x='gender', 
    y=crosstab_df.columns[1:], # Selects all experience columns automatically
    title='TikTok Shop Experience by Gender (Stacked Bar Chart)',
    labels={'gender': 'Gender', 'value': 'Count', 'variable': 'Experience'},
    color_discrete_sequence=px.colors.sequential.Viridis,
    template='plotly_white'
)

# 3. Update layout for better readability
fig.update_layout(
    xaxis_title="Gender",
    yaxis_title="Count",
    legend_title="TikTok Shop Experience",
    barmode='stack'
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
