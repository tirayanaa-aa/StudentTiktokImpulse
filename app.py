import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("📂 Navigation")

page_selection = st.sidebar.radio(
    "Select Page:",
    options=[
        "Main Page",
        "Objective 1 - Aina",
        "Objective 2 - Nurin",
        "Objective 3 - Nadia",
        "Objective 4 - Athirah"
    ]
)

# --------------------------------------------------
# Page Import & Display Logic
# --------------------------------------------------
if page_selection == "Main Page":
    import main
    main.app()  # Make sure main.py has an app() function

elif page_selection == "Objective 1 - Aina":
    import Objective1_Aina
    Objective1_Aina.app()

elif page_selection == "Objective 2 - Nurin":
    import Objective2_Nurin
    Objective2_Nurin.app()

elif page_selection == "Objective 3 - Nadia":
    import Objective3_Nadia
    Objective3_Nadia.app()

elif page_selection == "Objective 4 - Athirah":
    import Objective4_Athirah
    Objective4_Athirah.app()
