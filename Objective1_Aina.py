import plotly.express as px
import streamlit as st
import pandas as pd


def app():
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
    # Load and Clean Dataset
    # --------------------------------------------------
    try:
        df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")
        
        # CLEANING STEP: Remove leading/trailing spaces from column names
        df.columns = df.columns.str.strip()
        
        # DEBUG (Optional): Uncomment the line below to see all column names if error persists
        # st.write("Available columns:", df.columns.tolist())

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return

    # --------------------------------------------------
    # Sidebar Filter Options
    # --------------------------------------------------
    st.sidebar.header("Filter Options")

    # Use the actual column names from your CSV. 
    # If they are different (e.g., 'Age' instead of 'age_group'), change these variables:
    faculty_col = 'faculty'
    age_col = 'age_group' 

    # Faculty Filter
    faculty_list = ["All"] + sorted(df[faculty_col].dropna().unique().tolist())
    selected_faculty = st.sidebar.selectbox("Select Faculty", faculty_list)

    # Age Group Filter
    age_list = ["All"] + sorted(df[age_col].dropna().unique().tolist())
    selected_age = st.sidebar.selectbox("Select Age Group", age_list)

    # --------------------------------------------------
    # Data Filtering Logic
    # --------------------------------------------------
    filtered_df = df.copy()

    if selected_faculty != "All":
        filtered_df = filtered_df[filtered_df[faculty_col] == selected_faculty]
    
    if selected_age != "All":
        filtered_df = filtered_df[filtered_df[age_col] == selected_age]

    # --------------------------------------------------
    # Visualizations & Dynamic Interpretation
    # --------------------------------------------------
    st.divider()
    
    if filtered_df.empty:
        st.warning("No data found for the selected filters.")
    else:
        st.subheader("Gender Distribution")
        
        # Prepare Pie Chart Data
        gender_counts = filtered_df['gender'].value_counts().reset_index()
        gender_counts.columns = ['gender', 'count']

        fig1 = px.pie(
            gender_counts, 
            values='count', 
            names='gender', 
            title=f"Gender Distribution for {selected_faculty} (Age: {selected_age})",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.4
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Automated Interpretation
        total_n = gender_counts['count'].sum()
        top_gender = gender_counts.iloc[0]['gender']
        percentage = (gender_counts.iloc[0]['count'] / total_n) * 100

        st.info(f"""
        **Interpretation:** The pie chart reveals that the respondent pool for the selected criteria 
        is dominated by **{top_gender}s**, representing **{percentage:.1f}%** of the total (**n={total_n}**). 
        This suggests that marketing efforts should be specifically tailored toward this demographic.
        """)

# Execute the app
if __name__ == "__main__":
    app()
    
    # 2. Age Group Histogram
    st.subheader("Usage by Age")
    age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']
    fig2 = px.histogram(
        df, 
        x='age', 
        color='tiktok_shop_experience',
        barmode='group',
        category_orders={'age': age_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        title='TikTok Shop Usage across Age Groups'
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.write("""
    Interpretation:  
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
    Interpretation:  
   The bar chart for TikTok Shop Usage across Age Groups shows that the 22–26 years old group has the highest engagement, with a count of 80 users. This is significantly higher than the 17–21 years old group (under 20 users) and the 27–31 years old group, which shows the lowest activity.
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
    
    st.write("""
    Interpretation:  
   The data shows that TikTok Shop usage is predominantly driven by the 22–26 years old age group and students from the FSDK faculty. Most of these users fall into the lower income category of Under RM100, with participation rates declining as age and income levels increase.
    """)


# 5. TikTok Shop Experience by Gender
    st.subheader("TikTok Shop Experience by Gender")
    
    # Create the crosstab and reset index for Plotly
    crosstab_df = pd.crosstab(df['gender'], df['tiktok_shop_experience']).reset_index()

    # Create the Stacked Bar Chart
    fig5 = px.bar(
        crosstab_df, 
        x='gender', 
        y=crosstab_df.columns[1:], # Selects experience categories (e.g., Yes/No)
        title='TikTok Shop Experience by Gender (Stacked Bar Chart)',
        labels={'gender': 'Gender', 'value': 'Count', 'variable': 'Experience'},
        color_discrete_sequence=px.colors.qualitative.Set2,
        barmode='stack'
    )
    
    # Improve layout for Streamlit
    fig5.update_layout(
        xaxis_title="Gender",
        yaxis_title="Number of Respondents",
        legend_title="Experience",
        hovermode="x unified"
    )
    
    st.plotly_chart(fig5, use_container_width=True)

    st.write("""
    Interpretation: The stacked bar chart illustrates the distribution of TikTok Shop experience across genders. It allows us to see not only which gender has the highest representation in the dataset but also the proportion of users within each gender who have utilized TikTok Shop features, helping identify if a gender-based gap exists in platform adoption.
    """)







