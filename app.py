import streamlit as st
import Objective3_Nadia   # file member C
import Objective4_Athirah  # file member D

# Page configuration
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Study",
    layout="wide"
)

st.title("📊 Determinants of Students' Impulse Buying Behavior on TikTok Shop")

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to page:", 
    [
        "Main Page", 
        "Objective 3 – Nadia", 
        "Objective 4 – Athirah"
    ]
)

# Load member pages
if page == "Main Page":
    st.subheader("Project Overview")
    st.write(
        "This Streamlit dashboard presents a scientific visualization study on "
        "students' impulse buying behavior on TikTok Shop."
    )
elif page == "Objective 3 – Nadia":
    Objective3_Nadia.app()   # panggil function app() dari file Objective3_Nadia.py
elif page == "Objective 4 – Athirah":
    Objective4_Athirah.app()  # panggil function app() dari file Objective4_Athirah.py
