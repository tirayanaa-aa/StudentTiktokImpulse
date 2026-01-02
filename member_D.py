import pandas as pd
import plotly.express as px

# =========================
# 1. SCATTER PLOT + TREND LINE
# =========================
fig1 = px.scatter(
    df,
    x='PP_score',
    y='OIB_score',
    trendline='ols',
    title='Relationship between Product Presentation<br>and Impulse Buying Behavior on TikTok Shop',
    labels={
        'PP_score': 'Product Presentation Score (Visual Quality & Information)',
        'OIB_score': 'Impulse Buying Score (Spontaneous Purchasing)'
    }
)
fig1.show()


# =========================
# 2. CORRELATION HEATMAP
# =========================
corr = df[['SL_score', 'PP_score', 'OIB_score']].corr()

fig2 = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale='RdBu',
    zmin=-1,
    zmax=1,
    title='Correlation between Shopping Lifestyle, Product Presentation,<br>and Impulse Buying Behavior on TikTok Shop'
)
fig2.show()


# =========================
# 3. LIKERT STACKED BAR CHART
# =========================
likert_data = df[
    ['image_quality_influence',
     'product_description_quality',
     'multi_angle_visuals',
     'info_richness_support']
]

likert_long = likert_data.melt(
    var_name='Product Presentation Item',
    value_name='Agreement Level'
)

fi
