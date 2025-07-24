from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file    = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Yuxing Liu Resume .pdf"
profile_pic = current_dir / "assets" / "Visa Photo Copy.JPG"

# --- GENERAL SETTINGS ---
PAGE_TITLE   = "Digital CV | Yuxing Liu"
PAGE_ICON    = ":wave:"
NAME         = "Yuxing Liu"
DESCRIPTION  = (
    "B.S. in Mathematics-Computer Science (Minor: Data Science) at UC San Diego, expected June 2027. "
    "Research Assistant specializing in web scraping, quantitative analysis, and machine learning."
)
EMAIL        = "yuxingliu0826@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/yuxing-liu-profile"
GITHUB_URL   = "https://github.com/yuxing26liu"

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
try:
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CSS file not found: styles/main.css")

# --- LOAD ASSETS ---
PDFbyte = None
try:
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
except FileNotFoundError:
    st.info("Resume PDF not found; download button hidden until uploaded.")

profile_img = None
try:
    profile_img = Image.open(profile_pic)
except FileNotFoundError:
    st.warning("Profile image not found: assets/Visa Photo Copy.JPG")

# --- PROJECT GALLERY DATA ---
GALLERY = [
    {
        "title": "RunBuggy Internship Final Poster",
        "categories": ["Machine Learning Model", "Analysis & Visualization Report"],
        "img_path": current_dir / "assets" / "Runbuggy Final Poster.pdf",
        "link": None,
        "summary": "Final poster highlighting data integration, clustering, scoring models, and insights."
    },
    {
        "title": "Outage Severity Across the U.S.",
        "categories": ["Machine Learning Model", "Analysis & Visualization Report"],
        "img_path": current_dir / "assets" / "Screenshot 2025-07-04 at 2.20.45 PM.png",
        "link": "https://yuxing26liu.github.io/Power-Outage-Predictor/",
        "summary": "Interactive comparison of actual vs predicted power outage durations with error visualization."
    },
    {
        "title": "M&A Merger & Acquisition Predictor",
        "categories": ["Machine Learning Model"],
        "img_path": current_dir / "assets" / "Business Acquisition Prediction.PDF",
        "link": "https://github.com/yuxing26liu/Merge-and-Acquisitions",
        "summary": "AI-driven acquisition likelihood classification and DCF valuation pipeline."
    }
]

# --- PROFESSIONAL EXPERIENCE DATA ---
EXPERIENCE = [
    {
        "role": "Data System Analyst Assistant, CAIDA",
        "date": "Jun 2025 – Present",
        "bullets": [
            "Developed a data-cleaning pipeline to normalize and dedupe Yelp API addresses with fuzzy matching and geolocation checks.",
            "Built backend services for a React front-end to serve repair-site recommendations and composite quality scores."
        ]
    },
    {
        "role": "Data Analyst Intern – RunBuggy",
        "date": "Nov 2024 – May 2025",
        "bullets": [
            "Applied clustering (KMeans, DBSCAN) and PCA to segment and categorize site data for recommendation logic.",
            "Constructed an NLP pipeline (tokenization, TF-IDF, LDA) to analyze customer messages for insights.",
            "Deployed RESTful APIs to compute nearest site recommendations and ratings."
        ]
    },
    {
        "role": "Machine Learning Engineer, Menolearn Project",
        "date": "Apr 2024 – Oct 2024",
        "bullets": [
            "Collaborated on design and development of an AI-driven empathetic chatbot for menopause support, improving healthcare access.",
            "Partnered with healthcare professionals to integrate medical knowledge into decision-making algorithms, enhancing response accuracy."
        ]
    },
    {
        "role": "Research Assistant, School of Global Policy and Strategy, UCSD",
        "date": "Apr 2024 – Jun 2025",
        "bullets": [
            "Extended a Python-based web scraper to integrate multiple APIs for global media data collection.",
            "Performed quantitative analysis on 200+ social media profiles to detect manipulation patterns and new metrics."
        ]
    },
    {
        "role": "Software Developer, Association For Computing Machinery",
        "date": "Apr 2024 – Jun 2024",
        "bullets": [
            "Developed a custom travel-planner web app using Next.js, Google Maps API, and MongoDB, enhancing user personalization.",
            "Designed UI/UX prototypes in Figma and refined interfaces based on user feedback."
        ]
    },
    {
        "role": "Web Developer, Women In Coding Website Design Project Team",
        "date": "Jan 2024 – Apr 2024",
        "bullets": [
            "Built a multi-page ‘Study with Me’ timer application using HTML and CSS, prioritizing intuitive, user-friendly navigation.",
            "Implemented a fully responsive website layout across mobile, tablet, and desktop devices, ensuring 100% screen-size compatibility."
        ]
    },
    {
        "role": "System Team Member, Triton Racing",
        "date": "Oct 2023 – Jun 2024",
        "bullets": [
            "Engineered motor controllers with SolidWorks, optimizing vehicle performance and safety.",
            "Led high-voltage safety training, improving team compliance in electric vehicle development."
        ]
    }
]

# --- FUNCTIONS ---
def render_home():
    # Hero section
    col1, col2 = st.columns([1,2], gap="small")
    with col1:
        if profile_img:
            st.image(profile_img, width=200)
        if PDFbyte:
            st.download_button("📄 Download Resume", PDFbyte, file_name=resume_file.name, mime="application/pdf")
        st.markdown(
            f"<div style='display:flex;gap:1rem;'>"
            f"<a href='{LINKEDIN_URL}' target='_blank'><img src='https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/linkedin.svg' width='24'/></a>"
            f"<a href='{GITHUB_URL}' target='_blank'><img src='https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/github.svg' width='24'/></a>"
            f"<a href='mailto:{EMAIL}'><img src='https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/gmail.svg' width='24'/></a>"
            "</div>", unsafe_allow_html=True)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)

    # Education & Skills
    st.write("---")
    ce, cs = st.columns(2)
    with ce:
        st.subheader("Education")
        st.write("**University of California, San Diego**")
        st.write("_B.S. Mathematics-Computer Science (Minor: Data Science), Jun 2026_")
    with cs:
        st.subheader("Skills")
        st.write("- AWS, Python, R, SQL, Excel, NumPy, Pandas")
        st.write("- Web scraping, ML (scikit-learn), visualization (Plotly)")
        st.write("- Git, Agile, Tableau, SolidWorks")

    # Experience timeline
    st.write("---")
    st.subheader("Professional Experience")
    st.markdown(
        "<style>"
        ".timeline {position:relative;padding-left:40px;}"
        ".timeline:before {content:'';position:absolute;left:20px;top:0;bottom:0;width:2px;background:#437D9D;}"
        ".timeline-item {margin-bottom:2rem;position:relative;}"
        ".timeline-item:before {content:'';position:absolute;left:16px;top:18px;width:12px;height:12px;border:2px solid #437D9D;border-radius:50%;background:#fff;}"
        ".tl-content {margin-left:40px;background:#fff;padding:1rem;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1);}"
        "</style>", unsafe_allow_html=True)
    html = "<div class='timeline'>"
    for exp in EXPERIENCE:
        items = ''.join(f"<li>{b}</li>" for b in exp['bullets'])
        html += (
            "<div class='timeline-item'>"
            f"<div class='tl-content'><h4>{exp['role']}<span style='float:right;color:#666;font-size:0.9rem;'>{exp['date']}</span></h4>"
            f"<ul>{items}</ul></div></div>"
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    # Projects filter
    st.write("---")
    st.subheader("Projects")
    cats = ["All", "Machine Learning Model", "AWS Cloud Computing", "Analysis & Visualization Report"]
    sel = st.radio("Filter by:", cats, horizontal=True, key="project_filter")
    filtered = [p for p in GALLERY if sel == "All" or sel in p["categories"]]
    if not filtered:
        st.info("No projects in this category.")
    else:
        cols = st.columns(3, gap="small")
        for idx, proj in enumerate(filtered):
            with cols[idx % 3]:
                raw_path = proj['img_path']
                if isinstance(raw_path, str):
                    path = raw_path
                    suffix = Path(raw_path).suffix.lower()
                else:
                    path = raw_path.as_posix()
                    suffix = raw_path.suffix.lower()
                if suffix == '.pdf':
                    media = f"<embed src='{path}' width='100%' height='150' type='application/pdf'/>"
                else:
                    media = f"<img src='{path}' width='100%'/>"
                st.markdown(
                    f"<div class='project-card'>" +
                    media +
                    f"<h5 style='margin:0.5rem 0 0.25rem 0;'><a href='{proj.get('link','')}' target='_blank'>{proj['title']}</a></h5>" +
                    f"<p style='font-size:0.9rem;color:#555;'>{proj['summary']}</p></div>",
                    unsafe_allow_html=True)
    st.write("<div style='height:50px'></div>", unsafe_allow_html=True)


def render_projects():
    st.title("Projects & Accomplishments")
    st.write("---")
    for proj in GALLERY:
        link = proj.get('link')
        title = proj['title']
        if link:
            st.write(f"- [{title}]({link})")
        else:
            st.write(f"- {title}")

# --- NAVIGATION ---
t1, t2 = st.tabs(["Home", "Projects"])
with t1:
    render_home()
with t2:
    render_projects()
