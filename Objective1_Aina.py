import plotly.express as px
import streamlit as st

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



import plotly.express as px
import streamlit as st

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


