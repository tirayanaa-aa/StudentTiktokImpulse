import streamlit as st

st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Go to page:",
    [
        "Main Page",
        "Objective1_Aina",
        "Objective2_Nurin",
        "Objective3_Nadia",
        "Objective4_Athirah"
    ]
)

if page == "Main Page":
    import main

elif page == "Objective1_Aina":
    import Objective1_Aina
    Objective1_Aina.app()

elif page == "Objective2_Nurin":
    import Objective2_Nurin
    Objective2_Nurin.app()

elif page == "Objective3_Nadia":
    import Objective3_Nadia
    Objective3_Nadia.app()

elif page == "Objective4_Athirah":
    import Objective4_Athirah
    Objective4_Athirah.app()
