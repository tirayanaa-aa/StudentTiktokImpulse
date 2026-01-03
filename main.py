import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="TikTok Shop Impulse Buying Visualization",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("📊 Determinants of Students’ Impulse Buying Behavior on TikTok Shop")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.subheader("🎯 Project Overview")
st.write("""
This project investigates **students’ impulse buying behavior on TikTok Shop** using
scientific and interactive data visualization techniques.

The study aims to uncover key psychological, marketing, and demographic factors
that influence unplanned purchasing decisions on social commerce platforms.
""")

st.markdown("---")

# --------------------------------------------------
# Problem Statement
# --------------------------------------------------
st.subheader("📌 Problem Statement")
st.write("""
TikTok Shop has rapidly gained popularity among students by integrating entertainment,
product discovery, and instant purchasing within a single platform.
As a result, many students engage in impulse buying without prior planning.

However, the factors driving this behavior—such as promotions, trust, enjoyment,
product presentation, and personal shopping lifestyle—are not always clearly understood.
Without proper visualization and analysis, it is difficult to identify patterns,
relationships, and trends within impulse buying behavior.
""")

st.markdown("---")

# --------------------------------------------------
# Project Objectives
# --------------------------------------------------
st.subheader("🎯 Project Objectives")
st.markdown("""
**Main Objective:**  
To analyze and visualize the factors influencing students’ impulse buying behavior
on TikTok Shop using scientific data visualization techniques.

**Sub-Objectives:**
1. Analyze the demographic profile and TikTok Shop usage among students.  
2. Evaluate the influence of scarcity and unexpected product discovery.  
3. Examine the role of trust, enjoyment, and shopping motivation.  
4. Analyze the impact of product presentation and shopping lifestyle on impulse buying behavior.
""")

st.markdown("---")

# --------------------------------------------------
# Dataset Description
# --------------------------------------------------
st.subheader("📂 Dataset Description")
st.write("""
The dataset consists of survey responses collected from university students
using Google Forms.

- Data type: Likert-scale questionnaire  
- Respondents: University students  
- Focus: TikTok Shop shopping experience and behavior  
- Data preprocessing: Cleaning, renaming, and composite score calculation
""")

st.markdown("---")

# --------------------------------------------------
# Tools & Techniques
# --------------------------------------------------
st.subheader("🛠 Tools & Techniques")
st.markdown("""
- **Python** – Data processing and analysis  
- **Streamlit** – Interactive dashboard development  
- **Pandas** – Data manipulation  
- **Plotly / Matplotlib / Seaborn** – Scientific visualizations  
""")

st.markdown("---")

# --------------------------------------------------
# Navigation Guide
# --------------------------------------------------
st.subheader("🧭 Navigation Guide")
st.write("""
Use the **sidebar** to navigate through different sections of the dashboard:

- **Main Page** – Project overview and objectives  
- **Member Pages** – Each member focuses on a specific sub-objective  
  - Member A: Demographic profile & usage  
  - Member B: Scarcity & product discovery  
  - Member C: Trust & shopping motivation  
  - Member D: Product presentation & impulse buying
""")

st.info("📌 Please use the sidebar on the left to explore the analysis pages.")
