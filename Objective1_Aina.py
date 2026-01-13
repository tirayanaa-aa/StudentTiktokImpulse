import plotly.express as px
import streamlit as st
import pandas as pd



def app():
    st.header("Sub-Objective 1: Analyze the Demographic Profile and TikTok Shop Usage")

    # --------------------------------------------------
    # Load and Clean Dataset
    # --------------------------------------------------
    try:
        df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")
        df.columns = df.columns.str.strip()
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return

    # --------------------------------------------------
    # MAIN PAGE FILTER (Applies only to Pie Chart)
    # --------------------------------------------------
    st.divider()
    st.subheader("Filter Pie Chart")
    
    age_col = 'age' 
    age_list = ["All"] + sorted(df[age_col].dropna().unique().tolist())
    selected_age = st.selectbox("Select Age Group to filter Gender Distribution below:", age_list)

    # Filtering Logic for PIE CHART ONLY
    if selected_age != "All":
        pie_df = df[df[age_col] == selected_age]
    else:
        pie_df = df.copy()

    # --------------------------------------------------
    # 1. GENDER PIE CHART (Filtered by Age)
    # --------------------------------------------------
    st.divider()
    st.subheader("1. Gender Distribution")
    
    if pie_df.empty:
        st.warning(f"No data found for Age Group: {selected_age}")
    else:
        gender_counts = pie_df['gender'].value_counts().reset_index()
        gender_counts.columns = ['gender', 'count']

        fig1 = px.pie(
            gender_counts, values='count', names='gender', 
            title=f"Gender Proportion for Age Group: {selected_age}",
            color_discrete_sequence=px.colors.qualitative.Pastel, hole=0.4
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Dynamic Interpretation
        top_gender = gender_counts.iloc[0]['gender']
        percentage = (gender_counts.iloc[0]['count'] / len(pie_df)) * 100
        st.info(f"**Interpretation:** For the **{selected_age}** group, the population is dominated by **{top_gender}s** ({percentage:.1f}%).")

    # --------------------------------------------------
    # 2. AGE GROUP HISTOGRAM (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("2. Overall Usage by Age")
    age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']
    
    fig2 = px.histogram(
        df, x=age_col, color='tiktok_shop_experience', barmode='group',
        category_orders={age_col: age_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        title='TikTok Shop Usage across All Age Groups'
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    st.info("**Interpretation:** The histogram shows that the 22–26 years old group has the highest engagement. This provides a baseline comparison against the filtered gender data above.")

    # --------------------------------------------------
    # 3. Monthly Income Distribution (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("3. Monthly Income Distribution")
    income_order = df['monthly_income'].value_counts().index.tolist()
    fig3 = px.histogram(
        df, x='monthly_income',
        category_orders={'monthly_income': income_order},
        color='monthly_income', color_discrete_sequence=px.colors.sequential.Viridis,
        title='Overall Monthly Income Category Distribution'
    )
    st.plotly_chart(fig3, use_container_width=True)

    top_income = df['monthly_income'].value_counts().idxmax()
    st.info(f"**Interpretation:** The majority of the total respondents fall into the **{top_income}** income category, indicating a specific economic profile for the platform's user base.")

    # --------------------------------------------------
    # 4. Faculty Distribution (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("4. Distribution by Faculty")
    faculty_counts = df['faculty'].value_counts().reset_index()
    faculty_counts.columns = ['faculty', 'count']
    faculty_counts = faculty_counts.sort_values(by='count', ascending=True)

    fig4 = px.bar(
        faculty_counts, x='count', y='faculty', orientation='h',
        title='Distribution of Faculty (Total Respondents)',
        color='count', color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    top_faculty = faculty_counts.iloc[-1]['faculty']
    st.info(f







