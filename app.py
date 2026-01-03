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
        "Objective 1 - Aina",
        "Objective 2 - Member B",
        "Objective 3 - Member C",
        "Objective 4 - Member D"
    ]
)

if page == "Main Page":
    import main_page
    main_page.app()

elif page == "Objective 1 - Aina":
    import member_A
    member_A.app()

elif page == "Objective 2 - Member B":
    import member_B
    member_B.app()

elif page == "Objective 3 - Member C":
    import member_C
    member_C.app()

elif page == "Objective 4 - Member D":
    import member_D
    member_D.app()
