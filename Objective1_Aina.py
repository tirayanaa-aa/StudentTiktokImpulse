import plotly.express as px
import streamlit as st
import pandas as pd


import streamlit as st
import pandas as pd
import plotly.express as px

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
    # MAIN PAGE FILTER
    # --------------------------------------------------
    st.divider()
    st.subheader("Filter Dataset")
    
    age_col = 'age' 
    age_list = ["All"] + sorted(df[age_col].dropna().unique().tolist())
    selected_age = st.selectbox("Select Age Group to Filter Demographic Profile", age_list)

    # Filtering Logic
    if selected_age != "All":
        filtered_df = df[df[age_col] == selected_age]
    else:
        filtered_df = df.copy()

    # --------------------------------------------------
    # 1. GENDER PIE CHART
    # --------------------------------------------------
    st.divider()
    st.subheader("Gender Distribution")
    
    if filtered_df.empty:
        st.warning(f"No data found for Age: **{selected_age}**.")
    else:
        gender_counts = filtered_df['gender'].value_counts().reset_index()
        gender_counts.columns = ['gender', 'count']

        fig1 = px.pie(
            gender_counts, values='count', names='gender', 
            title=f"Gender Proportion for Age Group: {selected_age}",
            color_discrete_sequence=px.colors.qualitative.Pastel, hole=0.4
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # DYNAMIC INTERPRETATION
        top_gender = gender_counts.iloc[0]['gender']
        percentage = (gender_counts.iloc[0]['count'] / len(filtered_df)) * 100
        st.info(f"**Interpretation:** For the **{selected_age}** group, the population is dominated by **{top_gender}s** ({percentage:.1f}%).")

    # --------------------------------------------------
    # 2. AGE GROUP HISTOGRAM
    # --------------------------------------------------
    st.divider()
    st.subheader("Usage by Age")
    age_order = ['17 - 21 years old', '22 - 26 years old', '27 - 31 years old']
    
    fig2 = px.histogram(
        filtered_df, x=age_col, color='tiktok_shop_experience', barmode='group',
        category_orders={age_col: age_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=f'TikTok Shop Usage: {selected_age}'
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # DYNAMIC INTERPRETATION
    total_users = len(filtered_df)
    st.write(f"**Interpretation:** In the filtered segment (**{selected_age}**), there are **{total_users}** total respondents. This chart allows us to see how many within this specific age bracket have actual TikTok Shop experience compared to those who do not.")

    # --------------------------------------------------
    # 3. Monthly Income Distribution
    # --------------------------------------------------
    st.divider()
    st.subheader("Income Distribution")
    income_order = filtered_df['monthly_income'].value_counts().index.tolist()
    fig3 = px.histogram(
        filtered_df, x='monthly_income',
        category_orders={'monthly_income': income_order},
        color='monthly_income', color_discrete_sequence=px.colors.sequential.Viridis,
        title=f'Monthly Income Distribution for {selected_age}'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # DYNAMIC INTERPRETATION
    if not filtered_df.empty:
        top_income = filtered_df['monthly_income'].value_counts().idxmax()
        st.write(f"**Interpretation:** For respondents aged **{selected_age}**, the most common income category is **{top_income}**.")

    # --------------------------------------------------
    # 4. Faculty Distribution
    # --------------------------------------------------
    st.divider()
    st.subheader("Distribution by Faculty")
    faculty_counts = filtered_df['faculty'].value_counts().reset_index()
    faculty_counts.columns = ['faculty', 'count']
    faculty_counts = faculty_counts.sort_values(by='count', ascending=True)

    fig4 = px.bar(
        faculty_counts, x='count', y='faculty', orientation='h',
        title=f'Faculty Distribution for {selected_age}',
        color='count', color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    # DYNAMIC INTERPRETATION
    if not faculty_counts.empty:
        top_faculty = faculty_counts.iloc[-1]['faculty']
        st.write(f"**Interpretation:** Within the **{selected_age}** group, the highest number of users come from the **{top_faculty}** faculty.")

    # --------------------------------------------------
    # 5. TikTok Shop Experience by Gender
    # --------------------------------------------------
    st.divider()
    st.subheader("TikTok Shop Experience by Gender")
    crosstab_df = pd.crosstab(filtered_df['gender'], filtered_df['tiktok_shop_experience']).reset_index()

    fig5 = px.bar(
        crosstab_df, x='gender', y=crosstab_df.columns[1:], 
        title=f'Experience by Gender for {selected_age}',
        labels={'gender': 'Gender', 'value': 'Count', 'variable': 'Experience'},
        color_discrete_sequence=px.colors.qualitative.Set2, barmode='stack'
    )
    st.plotly_chart(fig5, use_container_width=True)

    st.write(f"**Interpretation:** This stacked bar chart shows the ratio of TikTok Shop adoption specifically for **{selected_age}** respondents, segmented by gender.")

# Execute the app
if __name__ == "__main__":
    app()







