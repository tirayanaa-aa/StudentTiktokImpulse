import plotly.express as px
import streamlit as st
import pandas as pd

def app():
    # Everything below this line is indented by 4 spaces
    st.header("Sub-Objective 1: Analyze the Demographic Profile and TikTok Shop Usage")

    # --------------------------------------------------
    # Problem Statement
    # --------------------------------------------------
    st.subheader("Problem Statement")
    st.write("""
    E-commerce platforms such as TikTok Shop serve users from diverse demographic backgrounds. 
    However, limited understanding of how factors such as gender, age group, faculty, and income 
    relate to TikTok Shop usage may reduce the effectiveness of targeted marketing strategies.
    """)

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    # Ensure this CSV file is in the same folder on GitHub
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    # 1. Gender Pie Chart
    st.subheader("Gender Distribution")
    gender_counts = df['gender'].value_counts().reset_index()
    gender_counts.columns = ['gender', 'count']

    fig1 = px.pie(
        gender_counts, 
        values='count', 
        names='gender', 
        title='Distribution of Gender',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Age Group Histogram
    st.subheader("Usage by Age")
    age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']
    fig2 = px.histogram(
        df, 
        x='age', 
        color='tiktok_shop_experience',
        barmode='group',
        category_orders={'age': age_order},
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='TikTok Shop Usage across Age Groups'
    )
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Monthly Income Distribution
    st.subheader("Income Distribution")
    income_order = df['monthly_income'].value_counts().index.tolist()
    fig3 = px.histogram(
        df, 
        x='monthly_income',
        category_orders={'monthly_income': income_order},
        color='monthly_income',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Monthly Income Category Distribution'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Faculty Distribution
    st.subheader("Distribution by Faculty")
    faculty_counts = df['faculty'].value_counts().reset_index()
    faculty_counts.columns = ['faculty', 'count']
    faculty_counts = faculty_counts.sort_values(by='count', ascending=True)

    fig4 = px.bar(
        faculty_counts, 
        x='count', 
        y='faculty', 
        orientation='h',
        title='Distribution of Faculty',
        color='count',
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig4, use_container_width=True)









