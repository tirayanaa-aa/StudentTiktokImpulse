import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.subheader("Member D – Impulse Buying Analysis")

    # ==================================================
    # SUB-OBJECTIVE & CONTEXT
    # ==================================================
    st.markdown("""
    ## 📌 Sub-Objective 4: Analyze Product Presentation, Lifestyle Factors, and Impulse Buying Behavior

    ### 🎯 Sub-Objective
    To analyze how product appearance, personal shopping lifestyle, and impulse buying tendencies influence spontaneous purchasing behavior on TikTok Shop.

    ### 🧩 Problem Statement
    Impulse buying is a significant outcome in social commerce platforms. However, the influence of product presentation and individual shopping lifestyle on impulse buying behavior is not always clearly understood, requiring visual analytics to uncover underlying patterns and relationships.

    ### 📋 Relevant Questionnaire Sections
    - **Section 7:** Personal Shopping Lifestyle (SL)  
    - **Section 8:** Product Appearance and Description (PP)  
    - **Section 9:** Impulse Buying Behavior (OIB)
    """)

    # --------------------------------------------------
    # Load dataset
    # --------------------------------------------------
    df = pd.read_csv("tiktok_impulse_buying_cleaned.csv")

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
            title='Likert Scale Response Distribution'
        )
        fig3.update_layout(
            xaxis_title='Product Presentation Items',
            yaxis_title='Number of Respondents'
        )
        st.plotly_chart(fig3, use_container_width=True)
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
    else:
        st.warning(f"Missing box plot columns: {missing_cols}")
