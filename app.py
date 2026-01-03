import streamlit as st 
import streamlit as st 
import Objective1_Aina
import Objective2_Nurin
import Objective3_Nadia
import Objective4_Athirah

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

elif page == "Objective 1 – Aina":
    Objective1_Aina.app()

elif page == "Objective 2 – Nurin":
    Objective2_Nurin.app()

elif page == "Objective 3 – Nadia":
    Objective3_Nadia.app()

elif page == "Objective 4 – Athirah":
    Objective4_Athirah.app()
    st.write(
    "This Streamlit dashboard presents a scientific visualization study on "
    "students' impulse buying behavior on TikTok Shop."
    )
elif page == "Member C":
    member_C.app()
elif page == "Member D":
    member_D.app() # ✅ panggil function app() dari member_D
