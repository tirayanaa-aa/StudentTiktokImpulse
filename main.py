import streamlit as st

def app():
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

st.markdown("""
### 🧾 Project Snapshot
- **Domain:** Social Commerce & Consumer Behavior  
- **Target Group:** University Students  
- **Platform:** TikTok Shop  
- **Data Type:** Survey (Likert-scale)  
- **Analysis Type:** Descriptive & Exploratory Visualization  
- **Total Sub-Objectives:** 4  
""")

# --------------------------------------------------
# Project Overview
# --------------------------------------------------
st.subheader("🎯 Project Overview")
st.write("""
This project investigates **students’ impulse buying behavior on TikTok Shop** using 
survey data and **scientific visualization techniques**.  

Impulse buying has become increasingly common on social commerce platforms like TikTok Shop, 
where entertainment, promotions, and instant purchasing are combined in a single environment.
Through interactive visualizations, this project aims to uncover patterns, relationships, 
and insights behind students’ purchasing behavior.
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
# Visualization Strategy
# --------------------------------------------------
st.subheader("📈 Visualization Strategy")
st.write("""
This project applies **scientific visualization principles** to transform raw survey data
into meaningful visual insights. Each visualization is carefully selected based on the
nature of the data and the analytical goal.

The visualizations are designed to:
- Compare groups (e.g., gender, age, usage)
- Show distributions and variability (e.g., box plots)
- Reveal relationships between variables (e.g., scatter plots)
- Highlight patterns and trends in impulse buying behavior
""")

st.markdown("""
**Visualization Techniques Used:**
- **Bar Charts** – Compare demographic groups and factor importance
- **Stacked / Grouped Bar Charts** – Compare TikTok Shop usage across demographics
- **Heatmaps** – Identify correlations between psychological factors
- **Box Plots** – Analyze response variability and distribution
- **Scatter Plots** – Examine relationships between trust, motivation, and impulse buying
- **Radar Charts** – Visualize multi-dimensional trust and motivation constructs
""")

st.markdown("---")
st.subheader("🎨 Dashboard Design Rationale")
st.markdown("""
An **interactive dashboard** is chosen instead of static charts to allow
users to actively explore patterns and relationships in the data.

**Design Considerations:**
- Interactivity enables filtering by gender and other demographics
- Multiple coordinated views allow comparison across variables
- Clean layout minimizes cognitive overload
- Consistent color usage improves readability and interpretation

**Why Streamlit?**
- Lightweight and reproducible
- Suitable for academic visualization projects
- Enables rapid development of interactive analytics dashboards
""")

# --------------------------------------------------
# Methodology Overview
# --------------------------------------------------
st.subheader("🔬 Methodology Overview")
st.markdown("""
This project follows a structured data visualization workflow:

1. **Data Collection** – Online questionnaire using Likert-scale items  
2. **Data Cleaning** – Handling missing values, renaming variables, and data validation  
3. **Feature Construction** – Creating composite scores for trust, motivation, and impulse buying  
4. **Visualization Design** – Selecting charts based on data type and analytical goal  
5. **Interactive Analysis** – Using filters to explore patterns dynamically  

This ensures that insights are **systematic, reproducible, and scientifically grounded**.
""")

# --------------------------------------------------
# Dataset Description
# --------------------------------------------------
st.subheader("📂 Dataset Description")
st.markdown("""
The dataset was collected through an online questionnaire distributed to university students.

**Dataset Characteristics:**
- Respondents: University students  
- Scale: 5-point Likert scale (Strongly Disagree – Strongly Agree)  
- Variables:
  - Demographics (gender, age, faculty, income)
  - TikTok Shop usage behavior
  - Psychological factors (trust, enjoyment, motivation)
  - Product presentation and impulse buying indicators

**Preprocessing Steps:**
- Removal of incomplete responses  
- Standardization of variable naming  
- Calculation of composite scores for key constructs
""")

st.markdown(st.markdown("""
**Dataset Summary:**
- Total Respondents: **113 students**
- Total Variables: **43 variables**
- Likert Scale: **1 (Strongly Disagree) – 5 (Strongly Agree)**
- Missing Values: **Removed during cleaning**
""")
)

# --------------------------------------------------
# Expected Insights
# --------------------------------------------------
st.subheader("🔍 Expected Insights & Outcomes")
st.write("""
Through interactive visualization, this project aims to:

- Identify which demographic groups are more active on TikTok Shop
- Understand how scarcity and product discovery trigger impulse buying
- Examine the role of trust and enjoyment in motivating purchases
- Analyze how product presentation influences unplanned buying behavior

These insights can help explain **why students are prone to impulse buying**
in social commerce environments like TikTok Shop.
""")

# --------------------------------------------------
# Limitations & Assumptions
# --------------------------------------------------
st.subheader("⚠️ Limitations & Assumptions")
st.markdown("""
While this project provides valuable insights, several limitations are acknowledged:

- The dataset is based on **self-reported survey responses**
- Respondents are limited to **students**, not the general population
- Cross-sectional data prevents causal conclusions
- Impulse buying behavior is measured via perception, not actual purchase logs

These limitations are considered during interpretation and discussion.
""")

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
# Project Team & Responsibilities
# --------------------------------------------------
st.subheader("👥 Project Team & Responsibilities")
st.markdown("""
This project was developed collaboratively, with each member responsible
for one analytical sub-objective.

- **Aina** – Demographics & TikTok Shop Usage  
- **Nurin** – Scarcity & Product Discovery  
- **Nadia** – Trust, Enjoyment & Motivation  
- **Athirah** – Product Presentation & Shopping Lifestyle  

Each section applies appropriate visualization techniques to answer
its assigned research objective.
""")

st.markdown("---")
st.subheader("🧑‍💻 How to Use This Dashboard")
st.markdown("""
To explore the findings effectively:

1. Use the **sidebar navigation** to switch between analysis sections
2. Apply **filters** (e.g., gender) where available to refine insights
3. Hover over charts to view exact values and details
4. Read the **interpretation text** below each visualization for guidance

Each chart is designed to answer a specific research question
and should be interpreted in context.
""")

# --------------------------------------------------
# Dashboard Structure & Navigation
# --------------------------------------------------
st.subheader("🧭 Dashboard Structure & Navigation")
st.markdown("""
The dashboard is organized by **research sub-objectives**, ensuring clarity and focus:

- **Main Page**  
  - Project background, objectives, and methodology  

- **Aina – Demographics & Usage**  
  - Respondent profile and TikTok Shop usage patterns  

- **Nurin – Scarcity & Discovery**  
  - Impact of limited offers and unexpected product exposure  

- **Nadia – Trust & Motivation**  
  - Psychological drivers of impulse buying  

- **Athirah – Presentation & Lifestyle**  
  - Visual presentation and shopping habits  

📌 Please use the sidebar on the left to explore the analysis pages.
""")

# ------------------------------------------------------------
# Reproducibility & Source Code
# ------------------------------------------------------------
st.subheader("📁 Reproducibility & Source Code")
st.markdown("""
The complete source code, dataset, and documentation for this project
are maintained in a GitHub repository.

This ensures:
- Transparency
- Reproducibility
- Proper version control
""")

# ------------------------------------------------------------
# Academic Note
# ------------------------------------------------------------
st.markdown("---")
st.info("""
📘 **Academic Note:**  
This project is conducted for educational purposes only.  
All data is anonymized and analyzed ethically to support learning in data visualization.
""")
