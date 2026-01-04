import plotly.express as px
import streamlit as st
import pandas as pd

def app():
    # Pastikan setiap baris di bawah ini mempunyai 4 ruang kosong (indent)
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
    
    # SAYA TELAH BETULKAN KURUNGAN DI SINI )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.write("""
    **Interpretation:**  
    The pie chart shows a significant gender imbalance, with females making up the vast majority at 78.8% compared to males at 21.2%. This indicates that the dataset is heavily dominated by female respondents, outnumbering males by nearly four to one.
    """)

    
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

    st.write("""
    **Interpretation:**  
    The bar chart reveals that the 22–26 years old age group has the highest TikTok Shop usage, with a count of approximately 80 respondents. In contrast, usage is significantly lower among the 17–21 and 27–31 age groups, indicating that the platform's shopping features are most popular among young adults in their mid-twenties.
    """)
    
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

     st.write("""
    **Interpretation:**  
   The bar chart reveals that the 22–26 years old age group has the highest TikTok Shop usage, with a count of approximately 80 respondents. In contrast, usage is significantly lower among the 17–21 and 27–31 age groups, indicating that the platform's shopping features are most popular among young adults in their mid-twenties.
    """)

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









