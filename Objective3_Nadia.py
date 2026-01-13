import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def app():
    st.subheader("Students' Impulse Buying Behavior on TikTok Shop")

    
    # ==================================================
    # SUB-OBJECTIVE & CONTEXT
    # ==================================================
    st.markdown("""
    ## 📌 Sub-Objective 3: Examine Trust, Enjoyment & Shopping Motivation on TikTok Shop

    ### 🎯 Sub-Objective
    To investigate the role of trust, enjoyment, and motivation in shaping users’ shopping experiences on TikTok Shop.

    ### 🧩 Problem Statement
    Trust and enjoyment are critical psychological factors influencing online shopping decisions. 
    A lack of consumer trust or low enjoyment levels may negatively affect purchasing behavior. 
    Therefore, visually analyzing these constructs can help identify patterns and insights in users’ shopping experiences on TikTok Shop.
    
    ### 📋 Relevant Questionnaire Sections
    - **Section 5:** Trust in TikTok Shop (TR)  
    - **Section 6:** Fun and Motivation in Shopping (HM)
    """)

    
    # ==================================================
    # LOAD DATASET
    # ==================================================
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    
    # ==================================================
    # DEFINE FACTORS GROUPS
    # ==================================================
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


    # ==================================================
    # CREATE COMPOSITE SCORES
    # ==================================================
    df['Trust_Score'] = df[trust_items].mean(axis=1)
    df['Motivation_Score'] = df[motivation_items].mean(axis=1)

     # 🔧 SAFETY: remove missing values (important)
    df = df.dropna(subset=['Trust_Score', 'Motivation_Score'])

    
    # ==================================================
    # SUMMARY METRICS
    # ==================================================
    st.markdown("## 📊 Summary Metrics")
    
    metric_cols = ['Trust_Score', 'Motivation_Score']
    missing_cols = [c for c in metric_cols if c not in df.columns]
    
    if not missing_cols:
        col1, col2 = st.columns(2)
    
        # Trust Score Metric
        col1.metric(
            label="Average Trust Score",
            value=f"{df['Trust_Score'].mean():.2f}",
            delta=f"{df['Trust_Score'].max() - df['Trust_Score'].min():.2f} range"
        )
    
        # Motivation Score Metric
        col2.metric(
            label="Average Motivation Score",
            value=f"{df['Motivation_Score'].mean():.2f}",
            delta=f"{df['Motivation_Score'].max() - df['Motivation_Score'].min():.2f} range"
        )
    
        # Descriptive statistics table
        st.markdown("### 🔍 Descriptive Statistics")
        summary_df = df[metric_cols].describe().round(2)
    
        # Style dataframe (same visual standard)
        styled_df = summary_df.style.background_gradient(cmap='Blues', axis=1)
        st.dataframe(styled_df, height=220)
    
    else:
        st.warning(f"Missing columns for summary metrics: {missing_cols}")

    
    # ==================================================
    # 1️⃣ CORRELATION HEATMAP
    # ==================================================
    st.markdown("### 1️⃣ Correlation Between Trust & Motivation Items")
    
    corr_items = trust_items + motivation_items
    missing_corr = [c for c in corr_items if c not in df.columns]
    
    if not missing_corr:
        corr = df[corr_items].corr()
    
        fig1 = px.imshow(
            corr,
            text_auto='.2f',
            zmin=-1,
            zmax=1,
            color_continuous_scale='RdBu',
            title='Correlation Matrix of Trust & Motivation Items'
        )
        st.plotly_chart(fig1, use_container_width=True)

        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>Trust-related items show moderate to strong positive correlations among themselves, which particularly between honesty and quality matching the product description.</li>
            <li>Motivation factors such as discounts and gifts are also strongly correlated with each other, indicating consistent promotional influence.</li>
            <li>Several trust items will demonstrate the moderate postive relationships with motivation variables, that will suggesting that the higher trust is associated with increased shopping motivation.</li>
            <li>However, the correlarions between trust and motivation are generally weaker than those within each construct, indicating that trust supports motivation rathen than directly driving it.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)
    else:
        st.warning(f"Missing columns for correlation: {missing_corr}")
        

    # ==================================================
    # 2️⃣ BAR CHART - TRUST ITEMS
    # ==================================================
    st.markdown("### 2️⃣ Average Trust Scores by Item")
    
    missing_trust = [c for c in trust_items if c not in df.columns]
    
    if not missing_trust:
        trust_means = df[trust_items].mean().reset_index()
        trust_means.columns = ['Trust Item', 'Mean Score']
    
        fig2 = px.bar(
            trust_means,
            x='Trust Item',
            y='Mean Score',
            title="Average Trust Scores"
        )
        st.plotly_chart(fig2, use_container_width=True)

        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>Overall, trust levels are positive, with all items scoring above the midpoint, which suggestes that the customers generally feel confident about the brand.</li>
            <li>The strongest area is product variety that meeting the customer needs, indicating that this offerings align well with what people are lookinh for.</li>
            <li>Trust in reliability, honesty, and quality matching the description is also solid, by showing the consistency between the promises and the actual experience.</li>
            <li>The slightly lower score for "no risk" suggests that while trust is high, some customers may still have minor concerns that could be addressed through clearer guarantees or communication.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)
        
    else:
        st.warning(f"Missing trust columns: {missing_trust}")

    
    # ==================================================
    # 3️⃣ BOX PLOT - TRUST RESPONSES
    # ==================================================
    st.markdown("### 3️⃣ Distribution of Trust Responses")
    if not missing_trust:
        trust_long = df[trust_items].melt(var_name='Trust Item', value_name='Response')
        fig3 = px.box(trust_long, x='Trust Item', y='Response', points='all', title='Trust Item Response Distribution')
        st.plotly_chart(fig3, use_container_width=True)

        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>Most trust items have median responses between 3 and 4, indicating an overall positive level of trust among respondents.</li>
            <li>The item related to product variety meeting needs shows a slightly higher median and wider spread, suggesting varied but generally favourable perceptions.</li>
            <li>Trust in seller honesty and product description accuracy demostrates relatively consistent responses, with fewer extreme values.</li>
            <li>Overall, the distribution indicate that respondents tend to agree with trust statements, although some variation exists across different trust dimensions.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)


    # ==================================================
    # 4️⃣ BAR CHART - MOTIVATION ITEMS
    # ==================================================
    st.markdown("### 4️⃣ Average Motivation Scores by Item")
    missing_mot = [c for c in motivation_items if c not in df.columns]
    if not missing_mot:
        mot_means = df[motivation_items].mean().reset_index()
        mot_means.columns = ['Motivation Item', 'Mean Score']
        fig4 = px.bar(mot_means, x='Motivation Item', y='Mean Score', title="Average Motivation Scores")
        st.plotly_chart(fig4, use_container_width=True)

        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>Discounts and promotions are the strongest motivator, clearly standing out as the main driver of customer interest.</li>
            <li>Gifts also play a meaningfull role, by showing that added value beyond the core product resonates well with customers.</li>
            <li>Relaxation and stress reduction score slightly lower, but still indicate moderate motivation rather than disinterest.</li>
            <li>Overall, customers appear more motivated by tangible incentives than emotional or lifestyle benefits.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)


    # ==================================================
    # 5️⃣ SCATTER PLOT - TRUST vs MOTIVATION (WITH TRENDLINE)
    # ==================================================
    st.markdown("### 5️⃣ Relationship Between Trust and Motivation")
    if 'Trust_Score' in df.columns and 'Motivation_Score' in df.columns:
        fig5 = px.scatter(
            df,
            x='Trust_Score',
            y='Motivation_Score',
            labels={'Trust_Score': 'Trust Score', 'Motivation_Score': 'Motivation Score'},
            title='Trust vs Motivation'
        )

        # Add manual trendline
        x = df['Trust_Score'].values
        y = df['Motivation_Score'].values
        m, b = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = m * x_line + b
        fig5.add_scatter(x=x_line, y=y_line, mode='lines', name='Trend Line', line=dict(width=3))
        st.plotly_chart(fig5, use_container_width=True)

         # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>The scatter plot shows a clear positive relationship between trust score and motivation score, as the higher levels are generally associated with the higher shopping motivation.</li>
            <li>The upward-sloping trend line indicates that the motivation tends to increase steadily as trust improves.</li>
            <li>Although some variation exists at similar trust levels, the overall pattern will remains the consistent across the data points.</li>
            <li>This suggests that trust will plays a supportive role in enhancing the consumers' motivation to shop on this platform.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)


    # ==================================================
    # 6️⃣ RADAR CHART - TRUST DIMENSIONS
    # ==================================================
    st.markdown("### 6️⃣ Trust Dimension Radar Chart")
    if not missing_trust:
        import matplotlib.pyplot as plt
        labels = trust_items
        values = trust_means['Mean Score'].tolist()
        values += values[:1]  # complete loop
        angles = np.linspace(0, 2 * np.pi, len(labels)+1)
        fig6, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
        ax.plot(angles, values, linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles[:-1] * 180/np.pi, labels)
        st.pyplot(fig6)

         # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #6366f1;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
            <li>Overall, trust levels are fairly strong across all dimensions, with no area showing serious weakness.</li>
            <li>Customers are feel most confident that the product variety meets their needs and that quality matches the description, that suggesting expectations are largely being met.</li>
            <li>Trust in honesty and reliability is also high, indicating the posistive perceptions of seller integrity.</li>
            <li>However, the slightly lower score on "no risk" that suggests some customers may still feel cautions, leaving room to strengthen reassurance and transparency.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)
