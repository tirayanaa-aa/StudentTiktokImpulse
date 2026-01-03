import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.header(
        "Sub-Objective 3: Examine Trust, Enjoyment & Shopping Motivation on TikTok Shop"
    )

    # --------------------------------------------------
    #  Problem Statement
    # --------------------------------------------------
    st.subheader("Problem Statement")
    st.write("""
    Trust and enjoyment are critical psychological factors influencing online shopping decisions. 
    A lack of consumer trust or low enjoyment levels may negatively affect purchasing behavior. 
    Therefore, visually analyzing these constructs can help identify patterns and insights in users’ shopping experiences on TikTok Shop.
    """)

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    # --------------------------------------------------
    # Define factor groups
    # --------------------------------------------------
    trust_items = [
        'trust_no_risk',
        'trust_reliable',
        'trust_variety_meets_needs',
        'trust_sells_honestly',
        'trust_quality_matches_description'
    ]

    motivation_items = [
        'relax_reduce_stress',
        'motivated_by_discount_promo',
        'motivated_by_gifts'
    ]

    # --------------------------------------------------
    # Create composite scores
    # --------------------------------------------------
    df['Trust_Score'] = df[trust_items].mean(axis=1)
    df['Motivation_Score'] = df[motivation_items].mean(axis=1)

     # 🔧 SAFETY: remove missing values (important)
    df = df.dropna(subset=['Trust_Score', 'Motivation_Score'])

    # --------------------------------------------------
    # Optional: In-page filter for gender (replacing sidebar)
    # --------------------------------------------------
    st.subheader("Filter Respondents by Gender")
    genders = df['gender'].unique().tolist()
    selected_genders = st.multiselect("Select Gender(s):", options=genders, default=genders)
    filtered_df = df[df['gender'].isin(selected_genders)]

    # --------------------------------------------------
    # 1️⃣ Correlation Heatmap
    # --------------------------------------------------
    st.subheader("1️⃣ Correlation Between Trust & Motivation Items")
    corr_items = filtered_df[trust_items + motivation_items].corr()
    fig1 = px.imshow(
        corr_items,
        text_auto=True,
        color_continuous_scale='RdBu_r'
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.write("""
    **Interpretation:**  
    The correlation heatmap supports the finding that trust-related factors such as reliability, honesty, and product quality are positively associated with motivation factors such as discounts and gifts.
    This indicates that higher trust increases shopping motivation on TikTok Shop.
    """)

    # --------------------------------------------------
    # 2️⃣ Bar Chart – Trust Item Means
    # --------------------------------------------------
    st.subheader("2️⃣ Average Trust Scores by Item")
    trust_means = filtered_df[trust_items].mean().reset_index()
    trust_means.columns = ['Trust Item', 'Mean Score']
    fig2 = px.bar(trust_means, x='Trust Item', y='Mean Score')
    st.plotly_chart(fig2, use_container_width=True)

    st.write("""
    **Interpretation:**  
    This bar chart compares the average trust scores across different trust dimensions.
    The results show that product variety and reliability receive the highest trust ratings,
    indicating these aspects are most important to respondents.
    """)

     # --------------------------------------------------
    # 3️⃣ Box Plot – Trust Distribution 
    # --------------------------------------------------
    st.subheader("3️⃣ Distribution of Trust Responses")
    trust_long = filtered_df[trust_items].melt(var_name='Trust Item', value_name='Response')
    fig_box = px.box(
        trust_long,
        x='Trust Item',
        y='Response'
    )
    st.plotly_chart(fig_box, use_container_width=True)

    st.write("""
    **Interpretation:**  
    The box plot shows variation in trust responses across different trust items.
    Some items have wider ranges, indicating mixed opinions, while others show more consistent responses. 
    This visualization highlights variability, medians, and outliers that cannot be observed using mean values alone.
    """)

    # --------------------------------------------------
    # 4️⃣ Bar Chart – Motivation Item Means
    # --------------------------------------------------
    st.subheader("4️⃣ Average Motivation Scores by Item")

    motivation_means = filtered_df[motivation_items].mean().reset_index()
    motivation_means.columns = ['Motivation Item', 'Mean Score']

    fig3 = px.bar(
        motivation_means,
        x='Motivation Item',
        y='Mean Score'
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.write("""
    **Interpretation:**  
    Discounts and promotions emerge as the strongest motivational factor, followed by gifts and stress reduction. 
    This indicates that promotional strategies are highly effective in motivating impulse purchases.
    """)

    # --------------------------------------------------
    # 5️⃣ Scatter Plot – Trust vs Motivation
    # --------------------------------------------------
    st.subheader("5️⃣ Relationship Between Trust and Motivation")

    # Scatter plot
    fig4 = px.scatter(
        filtered_df,
        x='Trust_Score',
        y='Motivation_Score',
        labels={
            'Trust_Score': 'Trust Score',
            'Motivation_Score': 'Motivation Score'
        }
    )
    
    # ---- ADD MANUAL REGRESSION LINE (NumPy) ----
    x = filtered_df['Trust_Score'].values
    y = filtered_df['Motivation_Score'].values
    
    # Calculate line of best fit
    m, b = np.polyfit(x, y, 1)
    
    # Create line values
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = m * x_line + b
    
    # Add line to plot
    fig4.add_scatter(
        x=x_line,
        y=y_line,
        mode='lines',
        name='Trend Line',
        line=dict(width=3)
    )
    
    st.plotly_chart(fig4, use_container_width=True)

    st.write("""
    **Interpretation:**  
    The scatter plot shows a positive relationship between trust and shopping motivation.
    As trust increases, motivation also increases, supporting the importance of trust
    as a psychological driver of impulse buying behavior.
    """)

    # --------------------------------------------------
    # 6️⃣ Radar Chart – Trust Dimensions
    # --------------------------------------------------
    st.subheader("6️⃣ Trust Dimension Radar Chart")

    labels = trust_items
    values = trust_means['Mean Score'].tolist()
    values += values[:1]

    angles = np.linspace(0, 2 * np.pi, len(labels) + 1)

    fig5, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)

    st.pyplot(fig5)

    st.write("""
    **Interpretation:**  
    The radar chart shows that trust dimensions are relatively balanced, with slightly higher scores for reliability and product quality, highlighting
    their importance in shaping overall trust.
    """)
