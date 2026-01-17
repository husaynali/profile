import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Hussein Ali (@husaynali)",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Remove padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 1200px;
    }
    
    /* Dark theme */
    .stApp {
        background-color: #000000;
        color: #e7e9ea;
    }
    
    /* Profile header */
    .profile-header {
        background: linear-gradient(rgba(102, 0, 153, 0.3), rgba(0, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=300&fit=crop');
        background-size: cover;
        background-position: center;
        height: 200px;
        border-radius: 0 0 16px 16px;
        margin: -1rem -2rem 0 -2rem;
        border: 1px solid #2f3336;
    }
    
    .profile-pic {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        border: 5px solid #000000;
        margin-top: -70px;
        margin-left: 20px;
        background-image: url('https://avatars.githubusercontent.com/u/206615568?v=4');
        background-size: cover;
        background-position: center;
    }
    
    .profile-info {
        padding: 20px;
    }
    
    .profile-name {
        font-size: 24px;
        font-weight: bold;
        color: #e7e9ea;
        margin: 0;
    }
    
    .profile-handle {
        font-size: 16px;
        color: #71767b;
        margin: 0;
    }
    
    .profile-bio {
        font-size: 16px;
        color: #e7e9ea;
        margin-top: 12px;
        line-height: 1.5;
    }
    
    .profile-meta {
        display: flex;
        gap: 20px;
        margin-top: 12px;
        font-size: 15px;
        color: #71767b;
        flex-wrap: wrap;
    }
    
    .profile-meta span {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    /* Tweet-like cards */
    .tweet-card {
        background-color: #000000;
        border: 1px solid #2f3336;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 16px;
        transition: background-color 0.2s;
    }
    
    .tweet-card:hover {
        background-color: #080808;
    }
    
    .tweet-header {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 12px;
    }
    
    .tweet-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background-image: url('https://avatars.githubusercontent.com/u/206615568?v=4');
        background-size: cover;
        background-position: center;
        flex-shrink: 0;
    }
    
    .tweet-author-info {
        flex: 1;
        min-width: 0;
    }
    
    .tweet-author-line {
        display: flex;
        align-items: center;
        gap: 4px;
        flex-wrap: wrap;
    }
    
    .tweet-name {
        font-weight: bold;
        color: #e7e9ea;
        font-size: 16px;
    }
    
    .tweet-handle {
        color: #71767b;
        font-size: 15px;
    }
    
    .tweet-content {
        color: #e7e9ea;
        font-size: 16px;
        line-height: 1.5;
        margin-bottom: 12px;
        margin-left: 60px;
    }
    
    .tweet-title {
        font-size: 18px;
        font-weight: bold;
        color: #e7e9ea;
        margin-bottom: 8px;
    }
    
    .tweet-image {
        width: 100%;
        border-radius: 16px;
        margin-top: 12px;
        margin-left: 60px;
        border: 1px solid #2f3336;
    }
    
    .tweet-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
        margin-left: 60px;
    }
    
    .tweet-tag {
        background-color: #6600991a;
        color: #9966cc;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 14px;
        border: 1px solid #66009930;
    }
    
    .tweet-links {
        display: flex;
        gap: 8px;
        margin-top: 12px;
        margin-left: 60px;
        flex-wrap: wrap;
    }
    
    .tweet-link-btn {
        background-color: #660099;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        transition: background-color 0.2s;
        border: none;
    }
    
    .tweet-link-btn:hover {
        background-color: #7700b3;
        text-decoration: none;
        color: white;
    }
    
    .tweet-actions {
        display: flex;
        gap: 60px;
        margin-top: 16px;
        padding-top: 12px;
        margin-left: 60px;
        border-top: 1px solid #2f3336;
    }
    
    .action-btn {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #71767b;
        cursor: pointer;
        transition: color 0.2s;
        font-size: 14px;
    }
    
    .action-btn:hover {
        color: #9966cc;
    }
    
    .liked {
        color: #f91880 !important;
    }
    
    /* Experience cards */
    .exp-card {
        background-color: #000000;
        border: 1px solid #2f3336;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .exp-header {
        display: flex;
        gap: 16px;
        align-items: flex-start;
    }
    
    .exp-icon {
        width: 48px;
        height: 48px;
        background-color: #6600991a;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        flex-shrink: 0;
    }
    
    .exp-details h3 {
        font-size: 20px;
        font-weight: bold;
        color: #e7e9ea;
        margin: 0;
    }
    
    .exp-details .company {
        color: #9966cc;
        font-weight: 600;
        margin-top: 4px;
    }
    
    .exp-details .meta {
        display: flex;
        gap: 16px;
        color: #71767b;
        font-size: 14px;
        margin-top: 8px;
        flex-wrap: wrap;
    }
    
    .exp-highlights {
        margin-top: 16px;
        margin-left: 64px;
    }
    
    .exp-highlights li {
        color: #e7e9ea;
        margin-bottom: 8px;
        line-height: 1.5;
    }
    
    /* Skills section */
    .skill-bar-container {
        margin-bottom: 20px;
    }
    
    .skill-bar-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
        font-size: 15px;
    }
    
    .skill-bar-header .name {
        font-weight: 600;
        color: #e7e9ea;
    }
    
    .skill-bar-header .percent {
        color: #71767b;
    }
    
    .skill-bar-bg {
        height: 8px;
        background-color: #2f3336;
        border-radius: 4px;
        overflow: hidden;
    }
    
    .skill-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #660099, #9966cc);
        border-radius: 4px;
        transition: width 1s ease-out;
    }
    
    /* Certification cards */
    .cert-card {
        background-color: #000000;
        border: 1px solid #2f3336;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 12px;
        display: flex;
        gap: 16px;
        align-items: flex-start;
    }
    
    .cert-icon {
        width: 48px;
        height: 48px;
        background-color: #6600991a;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        flex-shrink: 0;
    }
    
    .cert-details h4 {
        font-size: 18px;
        font-weight: bold;
        color: #e7e9ea;
        margin: 0;
    }
    
    .cert-details .issuer {
        color: #9966cc;
        margin-top: 4px;
    }
    
    .cert-details .date {
        color: #71767b;
        font-size: 14px;
        margin-top: 4px;
    }
    
    /* Award card */
    .award-card {
        background: linear-gradient(135deg, #66009920, #0066cc20);
        border: 1px solid #66009950;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #000000;
        border-bottom: 1px solid #2f3336;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #71767b;
        padding: 16px 0;
        font-weight: 600;
        border-bottom: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        color: #e7e9ea;
        border-bottom: 2px solid #660099;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: transparent;
        color: #71767b;
        border: none;
        border-radius: 20px;
        padding: 4px 12px;
        font-weight: normal;
        transition: color 0.2s;
    }
    
    .stButton > button:hover {
        color: #9966cc;
        background-color: transparent;
    }
    
    /* Links */
    a {
        color: #9966cc;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Mobile Responsive Design */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0rem;
            padding-right: 0rem;
            padding-top: 0rem;
        }
        
        .profile-header {
            height: 150px;
            border-radius: 0;
            margin: 0;
        }
        
        .profile-pic {
            width: 100px;
            height: 100px;
            border: 4px solid #000000;
            margin-top: -50px;
            margin-left: 16px;
        }
        
        .tweet-content,
        .tweet-image,
        .tweet-tags,
        .tweet-links,
        .tweet-actions {
            margin-left: 0;
        }
        
        .exp-highlights {
            margin-left: 0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for likes
if 'likes' not in st.session_state:
    st.session_state.likes = {}

def toggle_like(item_id):
    if item_id not in st.session_state.likes:
        st.session_state.likes[item_id] = 0
    st.session_state.likes[item_id] = 1 if st.session_state.likes[item_id] == 0 else 0

# Profile Header
st.markdown("""
<div class="profile-header"></div>
<div class="profile-pic"></div>
<div class="profile-info">
    <h1 class="profile-name">Hussein Ali</h1>
    <p class="profile-handle">@husaynali</p>
    <p class="profile-bio">
        Computer Science graduate and BI Developer with expertise in data analytics, visualization, and cloud technologies. 
        Skilled in Python, SQL, and modern BI tools (Power BI, Superset, Metabase). Passionate about transforming raw data into actionable insights.
    </p>
    <div class="profile-meta">
        <span>📍 Cairo, Egypt</span>
        <span>🌐 <a href="https://hussein-ali.pages.dev" target="_blank">hussein-ali.pages.dev</a></span>
        <span>📧 <a href="mailto:hire-hussein@proton.me">hire-hussein@proton.me</a></span>
        <span>📱 <a href="tel:+201012787537">+20 101 278 7537</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Posts", "💼 Projects", "💻 Experience", "🛠️ Skills", "🎓 Certifications"])

with tab1:
    # Welcome post
    st.markdown("""
    <div class="tweet-card">
        <div class="tweet-header">
            <div class="tweet-avatar"></div>
            <div class="tweet-author-info">
                <div class="tweet-author-line">
                    <span class="tweet-name">Hussein Ali</span>
                    <span class="tweet-handle">@husaynali · now</span>
                </div>
            </div>
        </div>
        <div class="tweet-content">
            Welcome to my portfolio! 👋 I'm a BI Developer and Data Analyst with a passion for turning complex data into clear, actionable insights. 
            Currently working at Etisalat Egypt, I specialize in building MIS dashboards, ETL pipelines, and predictive models. 
            Check out my projects below and let's connect!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button(f"{'❤️' if st.session_state.likes.get('intro', 0) == 1 else '🤍'} {st.session_state.likes.get('intro', 0) if st.session_state.likes.get('intro', 0) > 0 else ''}", key="like_intro"):
            toggle_like("intro")
            st.rerun()
    
    # Award
    st.markdown("""
    <div class="award-card">
        <div style="display: flex; gap: 12px; align-items: flex-start;">
            <div style="font-size: 32px;">🏆</div>
            <div>
                <h3 style="margin: 0; font-size: 18px; font-weight: bold;">3rd Place - Coursera Data Science Competition</h3>
                <p style="margin: 4px 0 0 0; color: #71767b; font-size: 14px;">December 2022</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    projects = [
        {
            "id": "udtracker",
            "name": "UdTracker – Udemy Courses Dashboard",
            "description": "Interactive Streamlit dashboard built for the Dataskool Challenge. Provides comprehensive KPIs and visualizations of Udemy course data including ratings, pricing, subscribers, and categories. Features real-time filtering and dynamic insights.",
            "tags": ["Python", "Streamlit", "Pandas", "Plotly", "Data Visualization"],
            "links": [
                {"label": "🔗 Live App", "url": "https://udtracker.streamlit.app/"}
            ],
            "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop"
        },
        {
            "id": "vrinda",
            "name": "Vrinda Store Sales Dashboard",
            "description": "Excel MIS dashboard analyzing sales performance across multiple dimensions: state, gender, sales channel, and product category. Automated KPIs and visualizations monitor order trends, cancellations, and customer demographics for data-driven retail insights.",
            "tags": ["Excel", "MIS", "Data Analysis", "KPI Tracking", "Visualization"],
            "links": [
                {"label": "📊 Live Dashboard", "url": "https://1drv.ms/x/c/6CE48FAEED9DCBB7/EXmE7mmBJbNOmhBELO_9ibsBmAu0Lu8NZsuylhlg1VnZAA?e=1cq1iP"}
            ],
            "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=400&fit=crop"
        },
        {
            "id": "callcenter",
            "name": "Call Center Performance Dashboard",
            "description": "Comprehensive Excel MIS dashboard tracking operational excellence metrics: call volumes, duration, revenue generation, customer satisfaction ratings, and individual agent performance. Delivers automated KPIs and visual insights for service quality monitoring.",
            "tags": ["Excel", "MIS", "Performance Analytics", "Customer Service", "KPIs"],
            "links": [
                {"label": "📊 Live Dashboard", "url": "https://1drv.ms/x/c/6CE48FAEED9DCBB7/EUE2l1R4Q8RBq5hUh6RHi78BZkdwg-z9Qg8EMjjKnV27nQ?e=c6AFvb"}
            ],
            "image": "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800&h=400&fit=crop"
        },
        {
            "id": "healthcare",
            "name": "Healthcare Operations Dashboard",
            "description": "Power BI dashboard analyzing U.S. healthcare operations (2019-2020). Tracks patient growth trajectories, medical expenses, CPT units, payer performance metrics, and revenue trends to optimize healthcare delivery and financial performance.",
            "tags": ["Power BI", "SQL", "Healthcare Analytics", "DAX", "ETL"],
            "links": [],
            "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop"
        },
        {
            "id": "m2assistant",
            "name": "M2 – The Medical Assistant",
            "description": "Full-stack AI system (Graduation Project) detecting 20+ diseases and symptoms using computer vision and deep learning. Integrated LLM generates comprehensive medical reports, treatment recommendations, and first-aid guidance for improved patient care.",
            "tags": ["Python", "Deep Learning", "Computer Vision", "LLM", "Healthcare AI"],
            "links": [],
            "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&h=400&fit=crop"
        }
    ]
    
    for project in projects:
        links_html = ''.join([f'<a href="{link["url"]}" target="_blank" class="tweet-link-btn">{link["label"]}</a>' for link in project["links"]])
        
        st.markdown(f"""
        <div class="tweet-card">
            <div class="tweet-header">
                <div class="tweet-avatar"></div>
                <div class="tweet-author-info">
                    <div class="tweet-author-line">
                        <span class="tweet-name">Hussein Ali</span>
                        <span class="tweet-handle">@husaynali · Featured Project</span>
                    </div>
                </div>
            </div>
            <div class="tweet-content">
                <div class="tweet-title">{project['name']}</div>
                {project['description']}
            </div>
            <img src="{project['image']}" class="tweet-image">
            <div class="tweet-tags">
                {''.join([f'<span class="tweet-tag">{tag}</span>' for tag in project['tags']])}
            </div>
            {f'<div class="tweet-links">{links_html}</div>' if links_html else ''}
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button(f"{'❤️' if st.session_state.likes.get(project['id'], 0) == 1 else '🤍'} {st.session_state.likes.get(project['id'], 0) if st.session_state.likes.get(project['id'], 0) > 0 else ''}", key=f"like_{project['id']}"):
                toggle_like(project['id'])
                st.rerun()

with tab3:
    experiences = [
        {
            "id": "exp1",
            "title": "MIS Specialist",
            "company": "Etisalat Egypt",
            "location": "Cairo (Onsite)",
            "period": "Oct 2025 - Present",
            "highlights": [
                "Developed and maintained MIS reports and dashboards to monitor operational, service, and financial KPIs for the Keeta project",
                "Analyzed performance trends, delivery SLAs, and cost metrics to identify inefficiencies and support decision-making"
            ]
        },
        {
            "id": "exp2",
            "title": "Data Analyst Intern",
            "company": "COB Solution",
            "location": "Cairo (Hybrid)",
            "period": "Feb 2023 - Aug 2023",
            "highlights": [
                "Analyzed healthcare billing and financial KPIs, identifying inefficiencies and saving costs",
                "Built automated Power BI dashboards, cutting manual reporting effort by 60%"
            ]
        },
        {
            "id": "exp3",
            "title": "Data Analyst Intern",
            "company": "Business Spike",
            "location": "Beni-Suef (Onsite)",
            "period": "Jul 2021 - Jan 2022",
            "highlights": [
                "Developed ML models forecasting financial trends with 85% accuracy, guiding investment strategies",
                "Built KPI dashboards in Power BI and Looker, improving data-driven decision-making"
            ]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="exp-card">
            <div class="exp-header">
                <div class="exp-icon">💼</div>
                <div class="exp-details">
                    <h3>{exp['title']}</h3>
                    <div class="company">{exp['company']}</div>
                    <div class="meta">
                        <span>📍 {exp['location']}</span>
                        <span>📅 {exp['period']}</span>
                    </div>
                </div>
            </div>
            <div class="exp-highlights">
                <ul style="margin: 0; padding-left: 20px;">
                    {''.join([f'<li>{highlight}</li>' for highlight in exp['highlights']])}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    # Skills Progress Bars
    st.markdown("<h3 style='color: #e7e9ea; margin-bottom: 20px;'>📈 Core Proficiencies</h3>", unsafe_allow_html=True)
    
    skills = {
        "Python": 90,
        "SQL": 85,
        "Power BI": 88,
        "Excel": 90,
        "Machine Learning": 80,
        "ETL Development": 85,
        "Data Visualization": 92
    }
    
    for skill, level in skills.items():
        st.markdown(f"""
        <div class="skill-bar-container">
            <div class="skill-bar-header">
                <span class="name">{skill}</span>
                <span class="percent">{level}%</span>
            </div>
            <div class="skill-bar-bg">
                <div class="skill-bar-fill" style="width: {level}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Technologies
    st.markdown("<h3 style='color: #e7e9ea; margin: 30px 0 20px 0;'>🔧 Technologies & Tools</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 30px;">
        <span class="tweet-tag">Python</span>
        <span class="tweet-tag">PostgreSQL</span>
        <span class="tweet-tag">MySQL</span>
        <span class="tweet-tag">MongoDB</span>
        <span class="tweet-tag">Metabase</span>
        <span class="tweet-tag">Apache Superset</span>
        <span class="tweet-tag">Power BI</span>
        <span class="tweet-tag">Excel</span>
        <span class="tweet-tag">Google Sheets</span>
        <span class="tweet-tag">Jupyter</span>
        <span class="tweet-tag">Git</span>
        <span class="tweet-tag">GitHub</span>
        <span class="tweet-tag">Docker</span>
        <span class="tweet-tag">AWS</span>
        <span class="tweet-tag">Azure</span>
        <span class="tweet-tag">GCP</span>
        <span class="tweet-tag">Pandas</span>
        <span class="tweet-tag">NumPy</span>
        <span class="tweet-tag">Matplotlib</span>
        <span class="tweet-tag">Seaborn</span>
        <span class="tweet-tag">Scikit-learn</span>
        <span class="tweet-tag">PyTorch</span>
        <span class="tweet-tag">Looker</span>
        <span class="tweet-tag">Jira</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Soft Skills
    st.markdown("<h3 style='color: #e7e9ea; margin-bottom: 20px;'>💡 Soft Skills</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
        <span class="tweet-tag">Problem Solving</span>
        <span class="tweet-tag">Communication</span>
        <span class="tweet-tag">Collaboration</span>
        <span class="tweet-tag">Adaptability</span>
        <span class="tweet-tag">Continuous Learning</span>
        <span class="tweet-tag">Critical Thinking</span>
    </div>
    """, unsafe_allow_html=True)

with tab5:
    certifications = [
        {"name": "Microsoft Machine Learning Engineer", "issuer": "DEPI", "date": "Oct 2024"},
        {"name": "Google Data Analytics Professional", "issuer": "Coursera", "date": "Jan 2023"},
        {"name": "Machine Learning Specialization", "issuer": "Coursera", "date": "Oct 2022"},
        {"name": "Data Analyst Track", "issuer": "ITI TechLeaps", "date": "Dec 2022"},
        {"name": "Machine Learning with Python", "issuer": "FreeCodeCamp", "date": "Sep 2022"},
        {"name": "Data Analysis with Python", "issuer": "FreeCodeCamp", "date": "Jul 2022"}
    ]
    
    for cert in certifications:
        st.markdown(f"""
        <div class="cert-card">
            <div class="cert-icon">🎓</div>
            <div class="cert-details">
                <h4>{cert['name']}</h4>
                <div class="issuer">{cert['issuer']}</div>
                <div class="date">{cert['date']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0; color: #71767b; border-top: 1px solid #2f3336; margin-top: 40px;">
    © 2026 Hussein Ali • Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
