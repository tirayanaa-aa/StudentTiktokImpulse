import streamlit as st
import member_C
import member_D  # ✅ import member_D supaya boleh dipanggil

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
    ["Main Page", "Member A", "Member B", "Member C", "Member D"]
)

# Load member pages
if page == "Main Page":
    st.subheader("Project Overview")
    st.write(
        "This Streamlit dashboard presents a scientific visualization study on "
        "students' impulse buying behavior on TikTok Shop."
    )
elif page == "Member C":
    member_C.app()
elif page == "Member D":
    member_D.app()  # ✅ panggil function app() dari member_D
