import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- Fungsi Visualisasi ---

def create_scatter_plot(df):
    fig = px.scatter(
        df, x='PP_score', y='OIB_score',
        trendline="ols",
        opacity=0.6,
        title='Relationship: Product Presentation & Impulse Buying',
        labels={'PP_score': 'Presentation Score', 'OIB_score': 'Impulse Buying Score'},
        template='plotly_white'
    )
    return fig

def create_correlation_heatmap(df):
    corr = df[['SL_score','PP_score','OIB_score']].corr()
    fig = px.imshow(
        corr, text_auto='.2f', color_continuous_scale='coolwarm',
        title='Correlation Matrix',
        template='plotly_white'
    )
    return fig

def create_likert_stacked_bar(df):
    cols = ['image_quality_influence', 'product_description_quality', 'multi_angle_visuals', 'info_richness_support']
    df_melted = df[cols].melt(var_name='Item', value_name='Response')
    df_counts = df_melted.groupby(['Item', 'Response']).size().reset_index(name='Count')
    fig = px.bar(df_counts, x='Item', y='Count', color='Response', barmode='stack',
                 title='Response Distribution: Product Presentation', template='plotly_white')
    return fig

def create_purchase_behavior_hist(df):
    cols = ['no_purchase_plan', 'no_purchase_intent', 'impulse_purchase']
    df_melted = df[cols].melt(var_name='Behavior', value_name='Agreement')
    fig = px.histogram(df_melted, x='Agreement', color='Behavior', barmode='group',
                       title='Distribution of Purchase Behavior', template='plotly_white')
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))
    return fig

def create_attraction_boxplot(df):
    cols = ['similar_to_famous_brand_attraction', 'new_product_urgency', 'brand_trust_influence', 'unique_design_attraction']
    df_melted = df[cols].melt(var_name='Factor', value_name='Score')
    fig = px.box(df_melted, x='Factor', y='Score', color='Factor',
                 title='Distribution of Attraction & Trust Factors', template='plotly_white')
    fig.update_layout(showlegend=False, xaxis_tickangle=-20)
    return fig

# --- FUNGSI UTAMA (PENTING: Nama harus app) ---
def app():
    st.header("📊 Member D: Detailed Analysis")
    
    # Memeriksa apakah data tersedia di session_state
    if 'df' in st.session_state:
        df = st.session_state.df
        
        # Menampilkan Grafik
        st.plotly_chart(create_scatter_plot(df), use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(create_correlation_heatmap(df), use_container_width=True)
        with col2:
            st.plotly_chart(create_likert_stacked_bar(df), use_container_width=True)
            
        st.plotly_chart(create_purchase_behavior_hist(df), use_container_width=True)
        st.plotly_chart(create_attraction_boxplot(df), use_container_width=True)
        
    else:
        st.error("Data tidak ditemukan. Silakan upload data di halaman utama atau pastikan data dimuat di app.py.")
        # Opsional: Berikan tombol upload jika data hilang
        uploaded_file = st.file_uploader("Upload CSV Data", type="csv")
        if uploaded_file:
            st.session_state.df = pd.read_csv(uploaded_file)
            st.rerun()
