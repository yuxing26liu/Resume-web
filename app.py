from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

# ─── PATHS & CONFIG ─────────────────────────────────────────────────────────────
BASE        = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE    = BASE / "styles" / "main.css"
RESUME_PDF  = BASE / "assets" / "Yuxing Liu Resume .pdf"
PROFILE_IMG = BASE / "assets" / "Visa Photo Copy.JPG"

st.set_page_config(
    page_title="Digital CV | Yuxing Liu",
    page_icon=":wave:",
    layout="wide"
)

# ─── LOAD CSS ───────────────────────────────────────────────────────────────────
if CSS_FILE.exists():
    st.markdown(f"<style>{CSS_FILE.read_text()}</style>", unsafe_allow_html=True)

# ─── LOAD ASSETS ───────────────────────────────────────────────────────────────
try:
    resume_bytes = RESUME_PDF.read_bytes()
except FileNotFoundError:
    resume_bytes = None

try:
    profile_img = Image.open(PROFILE_IMG)
except FileNotFoundError:
    profile_img = None

# ─── PROJECT GALLERY ────────────────────────────────────────────────────────────
GALLERY = [
    {
        "title": "RunBuggy Internship Final Poster",
        "img": BASE / "assets" / "Runbuggy Final Poster.png",
        "link": None,
        "summary": "Poster highlighting data integration, clustering, and scoring model insights."
    },
    {
        "title": "Outage Severity Across the U.S.",
        "img": BASE / "assets" / "Outage Prediction.png",
        "link": "https://yuxing26liu.github.io/Power-Outage-Predictor/",
        "summary": "Interactive plot comparing actual vs predicted outage durations."
    },
    {
        "title": "M&A Merger & Acquisition Predictor",
        "img": BASE / "assets" / "Acquisition.png",
        "link": "https://github.com/yuxing26liu/Merge-and-Acquisitions",
        "summary": "AI-driven acquisition likelihood classification & DCF valuation."
    },
]

# ─── SKILL LISTS ────────────────────────────────────────────────────────────────
languages   = ["Python","Java","JavaScript","HTML/CSS","C","Bash","R","STATA","Arduino"]
data_skills = ["pandas","numpy","tableau","Excel","AWS RDS/S3/Quicksight","scikit‑learn","matplotlib","pyarrow"]
web_skills  = ["React","MongoDB","Next.js","Streamlit","AWS Lambda","Docker"]

# ─── SIDEBAR NAV & CONTACT ───────────────────────────────────────────────────────
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects"], key="nav")

if resume_bytes:
    st.sidebar.download_button(
        "📄 Download Resume",
        data=resume_bytes,
        file_name=RESUME_PDF.name,
        mime="application/pdf"
    )

st.sidebar.markdown(
    """
    <div style='display:flex;justify-content:center;gap:1rem;'>
      <a href="https://www.linkedin.com/in/yuxing-liu-profile" target="_blank">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/linkedin.svg" width="24"/>
      </a>
      <a href="https://github.com/yuxing26liu" target="_blank">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/github.svg" width="24"/>
      </a>
      <a href="mailto:yuxingliu0826@gmail.com">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/gmail.svg" width="24"/>
      </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ─── HOME PAGE ─────────────────────────────────────────────────────────────────
if page == "Home":
    st.title("📊 Dashboard Overview")

    # KPI Metrics
    c1, c2, c3 = st.columns(3, gap="large")
    c1.metric("Languages Known",     len(languages))
    c2.metric("Data & Cloud Skills", len(data_skills))
    c3.metric("Web & DevOps Skills", len(web_skills))

    st.markdown("---")

    # Interactive Charts Row
    pc1, pc2 = st.columns(2, gap="large")

    # Work Experience Pie
    with pc1:
        exp_df = pd.DataFrame({
            "Category": ["Engineering Related","Data Related","Machine Learning","Software"],
            "Count":    [2, 3, 1, 1]
        })
        fig1 = px.pie(
            exp_df,
            names="Category",
            values="Count",
            title="Work Experience by Type",
            hover_data=["Count"],
            hole=0.4
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Projects Bar Chart
    with pc2:
        proj_df = pd.DataFrame({
            "Category": [
                "AWS Cloud Projects","Healthcare",
                "Business ML Models","Energy Optimization",
                "Travel App","Study App"
            ],
            "Count": [2,1,1,1,1,1]
        })
        fig2 = px.bar(
            proj_df,
            x="Category",
            y="Count",
            title="Projects by Category",
            color="Category",
            text="Count"
        )
        fig2.update_layout(xaxis_tickangle=-45, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # Skills Growth Over Time with Labels
    st.subheader("📈 Skills Growth Over Time")
    skill_growth = pd.DataFrame({
        "Year": [2020, 2021, 2022,   2023,                   2024],
        "Total Skills": [1,      2,      3,      5,                         8],
        "Learned": [
            "Python",
            "HTML/CSS",
            "React, Pandas",
            "Clustering, PCA, Decision Trees",
            "Docker, AWS, PyArrow, PySpark"
        ]
    })
    fig3 = px.line(
        skill_growth,
        x="Year",
        y="Total Skills",
        markers=True,
        title="Cumulative Skills by Year",
        custom_data=["Learned"]
    )
    fig3.update_traces(
        hovertemplate=
            "<b>Year:</b> %{x}<br>"
            "<b>Total:</b> %{y}<br>"
            "<b>Learned:</b> %{customdata[0]}"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # Summary & Skills Breakdown
    left, right = st.columns([1, 2], gap="large")
    with left:
        if profile_img:
            st.image(profile_img, width=200)
        st.subheader("👤 Summary")
        st.write(
            "Passionate Data Scientist & Engineer with a foundation in machine learning, web scraping, "
            "quantitative analysis, and full‑stack development. Skilled at building scalable pipelines "
            "and interactive dashboards."
        )
        st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

    with right:
        st.subheader("🛠️ Skills Breakdown")
        s1, s2, s3 = st.columns(3, gap="large")
        with s1:
            st.markdown("**Coding Languages**")
            for lang in languages:
                st.write(f"- {lang}")
        with s2:
            st.markdown("**Data & Cloud**")
            for sk in data_skills:
                st.write(f"- {sk}")
        with s3:
            st.markdown("**Web & DevOps**")
            for sk in web_skills:
                st.write(f"- {sk}")

# ─── PROJECTS PAGE ─────────────────────────────────────────────────────────────
else:
    st.title("🎯 Projects")
    st.markdown("---")
    cols = st.columns(3, gap="medium")
    for idx, proj in enumerate(GALLERY):
        with cols[idx % 3]:
            path = proj["img"].as_posix() if isinstance(proj["img"], Path) else proj["img"]
            st.image(path, use_container_width=True)
            st.markdown(f"**[{proj['title']}]({proj.get('link','')})**")
            st.write(proj["summary"])
            st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)
