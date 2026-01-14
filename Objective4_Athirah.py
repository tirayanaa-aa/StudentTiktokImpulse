import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.subheader("Impulse Buying Analysis")

    
    # ==================================================
    # SUB-OBJECTIVE & CONTEXT
    # ==================================================
    st.markdown("""
    ## Sub-Objective 4: Analyze Product Presentation, Lifestyle Factors, and Impulse Buying Behavior
    To analyze how product appearance, personal shopping lifestyle, and impulse buying tendencies influence spontaneous purchasing behavior on TikTok Shop.

    ### Problem Statement
    Impulse buying is a significant outcome in social commerce platforms. However, the influence of product presentation and individual shopping lifestyle on impulse buying behavior is not always clearly understood, requiring visual analytics to uncover underlying patterns and relationships.

    ### Relevant Questionnaire Sections
    - **Section 7:** Personal Shopping Lifestyle (SL)  
    - **Section 8:** Product Appearance and Description (PP)  
    - **Section 9:** Impulse Buying Behavior (OIB)
    """)

    
    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

    
    # =========================
    # SUMMARY METRICS
    # =========================
    st.markdown("## 📊 Summary Metrics")

    metric_cols = ['SL_score', 'PP_score', 'OIB_score']
    missing_cols = [c for c in metric_cols if c not in df.columns]

    if not missing_cols:
        col1, col2, col3 = st.columns(3)

        # Add delta = 0 just for nicer look
        col1.metric(
            label="Average Lifestyle Score (SL)",
            value=f"{df['SL_score'].mean():.2f}",
        )

        col2.metric(
            label="Average Product Presentation Score (PP)",
            value=f"{df['PP_score'].mean():.2f}",
        )

        col3.metric(
            label="Average Impulse Buying Score (OIB)",
            value=f"{df['OIB_score'].mean():.2f}",
        )

        st.markdown("### 🔍 Descriptive Statistics")
        summary_df = df[metric_cols].describe().round(2)

        # Style dataframe
        styled_df = summary_df.style.background_gradient(cmap='Blues', axis=1)
        st.dataframe(styled_df, height=220)

    else:
        st.warning(f"Missing columns for summary metrics: {missing_cols}")


    
    # =========================
    # 1. SCATTER PLOT + TREND LINE
    # =========================
    st.markdown("### 1️⃣ Relationship Between Product Presentation and Impulse Buying")
    if 'PP_score' in df.columns and 'OIB_score' in df.columns:
        fig1 = px.scatter(
            df,
            x='PP_score',
            y='OIB_score',
            trendline='ols',
            labels={
                'PP_score': 'Product Presentation Score',
                'OIB_score': 'Impulse Buying Score'
            },
            title='Product Presentation vs Impulse Buying'
        )
        st.plotly_chart(fig1, use_container_width=True)
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
            <li>The scatter plot shows a positive relationship between product presentation and impulse buying behavior.</li>
            <li>Higher product presentation scores are generally associated with higher impulse buying scores.</li>
            <li>Most respondents fall within the medium to high score range, indicating strong visual influence.</li>
            <li>The spread of data points suggests that impulse buying is also affected by other personal or situational factors.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("PP_score or OIB_score column missing in dataset!")

    
    # =========================
    # 2. CORRELATION HEATMAP
    # =========================
    st.markdown("### 2️⃣ Correlation Between Key Constructs")
    corr_cols = ['SL_score', 'PP_score', 'OIB_score']
    missing_cols = [c for c in corr_cols if c not in df.columns]
    if not missing_cols:
        corr = df[corr_cols].corr()
        fig2 = px.imshow(
            corr,
            text_auto='.2f',
            zmin=-1,
            zmax=1,
            color_continuous_scale='RdBu',
            title='Correlation Matrix'
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
            <li>Shopping lifestyle shows a positive relationship with product presentation, indicating that students who enjoy shopping are more responsive to visual and informational cues.</li>
            <li>Product presentation has a weak to moderate correlation with impulse buying, suggesting that attractive visuals alone may not always trigger impulsive purchases.</li>
            <li>Shopping lifestyle demonstrates a stronger association with impulse buying compared to product presentation.</li>
            <li>This pattern highlights that personal shopping habits play a more influential role in impulse buying behaviour on TikTok Shop.</li>
        </ul>
        </div>
         """, unsafe_allow_html=True)

    else:
        st.warning(f"Missing columns for correlation: {missing_cols}")

    
    # =========================
    # 3. LIKERT STACKED BAR CHART
    # =========================
    st.markdown("### 3️⃣ Product Presentation Item Responses")
    likert_cols = [
        'image_quality_influence',
        'product_description_quality',
        'multi_angle_visuals',
        'info_richness_support'
    ]
    missing_cols = [c for c in likert_cols if c not in df.columns]
    if not missing_cols:
        likert_long = df[likert_cols].melt(
            var_name='Item',
            value_name='Agreement Level'
        )
        fig3 = px.histogram(
            likert_long,
            x='Item',
            color='Agreement Level',
            barmode='stack',
            title='Likert Scale Response Distribution',
            category_orders={
                'Agreement Level': [1, 2, 3, 4, 5]
            }
        )
        fig3.update_layout(
            xaxis_title='Product Presentation Items',
            yaxis_title='Number of Respondents'
        )
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
           <li>Most respondents selected higher agreement levels (4 and 5) across all product presentation items.</li>
           <li>Image quality and product description show particularly strong positive responses, indicating their importance in online purchasing decisions.</li>
           <li>Multi-angle visuals and rich product information also receive consistent agreement, suggesting that detailed visual presentation enhances consumer confidence.</li>
           <li>Overall, the distribution reflects that well-presented products on TikTok Shop play a key role in encouraging impulse buying behaviour.</li>
       </ul>
       </div>
       """, unsafe_allow_html=True)

    else:
        st.warning(f"Missing Likert columns: {missing_cols}")


    # =========================
    # 4. MULTI HISTOGRAM – PURCHASE BEHAVIOR
    # =========================
    st.markdown("### 4️⃣ Purchase Behaviour Distribution")
    purchase_cols = ['no_purchase_plan', 'no_purchase_intent', 'impulse_purchase']
    missing_cols = [c for c in purchase_cols if c not in df.columns]
    if not missing_cols:
        purchase_long = df[purchase_cols].melt(
            var_name='Purchase Type',
            value_name='Score'
        )
        fig4 = px.histogram(
            purchase_long,
            x='Score',
            color='Purchase Type',
            barmode='overlay',
            nbins=5,
            title='Distribution of Purchase Behaviour'
        )
        fig4.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            yaxis_title='Number of Respondents'
        )
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
           <li>Most respondents show moderate to high agreement (levels 3 to 5) across all impulse buying indicators.</li>
           <li>The highest concentration of responses appears at agreement levels 4 and 5, especially for impulse purchase behavior.</li>
           <li>This pattern indicates that many purchases on TikTok Shop are made without prior planning or strong purchase intent.</li>
           <li>Overall, the visualization highlights impulse buying as a common behavior among users, supporting the study’s focus on spontaneous purchasing in social commerce.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning(f"Missing purchase columns: {missing_cols}")
                     

    # =========================
    # 5. BOX PLOT – PRODUCT & BRAND FACTORS
    # =========================
    st.markdown("### 5️⃣ Product & Brand Attraction Factors")
    box_cols = [
        'similar_to_famous_brand_attraction',
        'new_product_urgency',
        'brand_trust_influence',
        'unique_design_attraction'
    ]
    missing_cols = [c for c in box_cols if c not in df.columns]
    if not missing_cols:
        box_long = df[box_cols].melt(
            var_name='Factor',
            value_name='Score'
        )
        fig5 = px.box(
            box_long,
            x='Factor',
            y='Score',
            points='outliers',
            title='Distribution of Product Attraction & Trust Factors'
        )
        fig5.update_layout(
            yaxis_title='Score (1 = Strongly Disagree, 5 = Strongly Agree)'
        )
        st.plotly_chart(fig5, use_container_width=True)
        # -------------------------
        # INTERPRETATION / INSIGHTS
        # -------------------------
        st.markdown("""
        <div style="
            background-color:#f8fafc;
            padding:16px;
            border-left:6px solid #10b981;
            border-radius:10px;
            box-shadow:0 2px 6px rgba(0,0,0,0.05);
            margin-top:10px;
        ">
        <h4 style="margin-bottom:8px;">📌 Key Insights</h4>

        <ul style="margin-left:15px;">
           <li>The box plot shows that the median scores for all factors are around level 3 to 4, indicating moderate to high agreement among respondents.</li>
           <li><em>Brand trust influence</em> and <em>unique design attraction</em> exhibit relatively consistent distributions, suggesting these factors are commonly perceived as important.</li>
           <li><em>New product urgency</em> shows a wider spread, indicating varying levels of influence across respondents.</li>
           <li>Several low-score outliers are observed, suggesting that a small group of students is less affected by brand-related attraction factors.</li>
           <li>Overall, the visualization indicates that product attraction and trust play a meaningful role in shaping impulse buying behaviour on TikTok Shop.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning(f"Missing box plot columns: {missing_cols}")
