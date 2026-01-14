import plotly.express as px
import streamlit as st
import pandas as pd


def app():
    # --------------------------------------------------
    # Header & Introduction
    # --------------------------------------------------
    st.header("📌 Sub-Objective 1: Analyze the Demographic Profile and TikTok Shop Usage")

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
        # Cleaning column names to prevent KeyError: 'age_group'
        df.columns = df.columns.str.strip() 
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return

    # --------------------------------------------------
    # MAIN PAGE FILTER (Applies only to Pie Chart)
    # --------------------------------------------------
    st.divider()
    st.subheader("🔍 Filter Demographic Profile")
    
    # Define variables before use to prevent UnboundLocalError
    age_col = 'age' 
    gender_col = 'gender'
    
    age_list = ["All"] + sorted(df[age_col].dropna().unique().tolist())
    selected_age = st.selectbox("Select Age Group to filter Gender Distribution below:", age_list)

    # Filtering Logic for PIE CHART ONLY
    if selected_age != "All":
        pie_df = df[df[age_col] == selected_age]
    else:
        pie_df = df.copy()

    # --------------------------------------------------
    # EXECUTIVE SUMMARY 📋
    # --------------------------------------------------
    st.subheader("📋 Summary")
    
    total_respondents = len(df)
    filtered_n = len(pie_df)
    active_users = len(df[df['tiktok_shop_experience'] == 'Yes'])
    usage_rate = (active_users / total_respondents) * 100

    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Total Sample", total_respondents)
    col_m2.metric(f"Filtered ({selected_age})", filtered_n)
    col_m3.metric("Platform Usage", f"{usage_rate:.1f}%")

    st.info(f"**Quick Insight:** 💡 Out of **{total_respondents}** participants, **{usage_rate:.1f}%** have experience using TikTok Shop. You are currently analyzing the **{selected_age}** demographic segment.")

    # --------------------------------------------------
    # 1. GENDER PIE CHART (Filtered by Age)
    # --------------------------------------------------
    st.divider()
    st.subheader("1. 📊 Gender Distribution")
    
    if pie_df.empty:
        st.warning(f"No data found for Age Group: {selected_age}")
    else:
        gender_counts = pie_df[gender_col].value_counts().reset_index()
        gender_counts.columns = [gender_col, 'count']

        fig1 = px.pie(
            gender_counts, values='count', names=gender_col, 
            title=f"Gender Proportion (Age: {selected_age})",
            color_discrete_sequence=px.colors.qualitative.Pastel, hole=0.4
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        top_gender = gender_counts.iloc[0][gender_col]
        percentage = (gender_counts.iloc[0]['count'] / len(pie_df)) * 100
        st.info(f"**Interpretation:** 🎯 For the **{selected_age}** group, the sample is dominated by **{top_gender}s** ({percentage:.1f}%).The pie chart reveals that the respondent pool is dominated by [Gender], representing [Percentage]% of the total. This suggests that marketing efforts should be tailored toward this specific demographic")

    # --------------------------------------------------
    # 2. AGE GROUP HISTOGRAM (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("2. 🕒 Overall Usage by Age")
    age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']
    
    fig2 = px.histogram(
        df, x=age_col, color='tiktok_shop_experience', barmode='group',
        category_orders={age_col: age_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        title='TikTok Shop Usage Trend'
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.info("**Interpretation:** 🚀 The **22–26 age group** consistently represents the highest engagement level on the platform.")

    # --------------------------------------------------
    # 3. Monthly Income Distribution (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("3. 💰 Monthly Income Distribution")
    income_order = df['monthly_income'].value_counts().index.tolist()
    fig3 = px.histogram(
        df, x='monthly_income',
        category_orders={'monthly_income': income_order},
        color='monthly_income', color_discrete_sequence=px.colors.sequential.Viridis,
        title='Income Category Distribution'
    )
    st.plotly_chart(fig3, use_container_width=True)

    top_income = df['monthly_income'].value_counts().idxmax()
    st.info(f"**Interpretation:** 💵 The bar chart for TikTok Shop Usage across Age Groups shows that the 22–26 years old group has the highest engagement, with a count of 80 users. This is significantly higher than the 17–21 years old group (under 20 users) and the 27–31 years old group, which shows the lowest activity.")

  # --------------------------------------------------
    # 4. 🎓 Distribution by Faculty
    # --------------------------------------------------
    st.divider()
    st.subheader("4. 🎓 Distribution by Faculty")

    # Define your official survey faculty list
    official_faculties = ['FKP', 'FTKW', 'FSB', 'FHPK', 'FBI', 'FSDK']

    # Create a copy for processing
    faculty_df = df.copy()

    # Logic to group everything else into 'Other'
    faculty_df['faculty_cleaned'] = faculty_df['faculty'].apply(
        lambda x: x if x in official_faculties else 'Other'
    )

    # Count the cleaned faculty data
    faculty_counts = faculty_df['faculty_cleaned'].value_counts().reset_index()
    faculty_counts.columns = ['faculty', 'count']
    
    # Sort so the highest is at the top of the horizontal bar
    faculty_counts = faculty_counts.sort_values(by='count', ascending=True)

    fig4 = px.bar(
        faculty_counts, 
        x='count', 
        y='faculty', 
        orientation='h',
        title='User Distribution by Official Faculty Categories',
        color='count', 
        color_continuous_scale='Viridis',
        # Ensure 'Other' stays at the bottom or top consistently if preferred
        category_orders={'faculty': ['Other'] + official_faculties} 
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Dynamic Interpretation
    top_faculty = faculty_counts.iloc[-1]['faculty']
    st.info(f"**Interpretation:** 🏫 The **{top_faculty}** faculty shows the highest participation rate in this survey. Responses from smaller departments or unofficial entries have been grouped into **'Other'** to match the core survey structure.")

    # --------------------------------------------------
    # 5. TikTok Shop Experience by Gender (Independent)
    # --------------------------------------------------
    st.divider()
    st.subheader("5. 👩‍💻 Experience by Gender")
    crosstab_df = pd.crosstab(df[gender_col], df['tiktok_shop_experience']).reset_index()

    fig5 = px.bar(
        crosstab_df, x=gender_col, y=crosstab_df.columns[1:], 
        title='Experience Ratio per Gender',
        labels={gender_col: 'Gender', 'value': 'Count', 'variable': 'Experience'},
        color_discrete_sequence=px.colors.qualitative.Set2, barmode='stack'
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.info("**Interpretation:** 🤝 This chart identifies the platform adoption rate, showing how experience levels differ between male and female users.")

if __name__ == "__main__":
    app()





