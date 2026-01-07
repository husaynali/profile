import streamlit as st
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Hussein Ali (@husaynali)",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to make it look like Twitter
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
        background: linear-gradient(rgba(29, 155, 240, 0.3), rgba(0, 0, 0, 0.8)), 
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
        align-items: center;
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
    }
    
    .tweet-author {
        flex: 1;
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
    }
    
    .tweet-image {
        width: 100%;
        border-radius: 16px;
        margin-top: 12px;
        border: 1px solid #2f3336;
    }
    
    .tweet-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }
    
    .tweet-tag {
        background-color: #1d9bf015;
        color: #1d9bf0;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 14px;
        border: 1px solid #1d9bf030;
    }
    
    .tweet-actions {
        display: flex;
        gap: 60px;
        margin-top: 16px;
        padding-top: 12px;
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
        color: #1d9bf0;
    }
    
    .liked {
        color: #f91880 !important;
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
        border-bottom: 2px solid #1d9bf0;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #1d9bf0;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 16px;
        font-weight: bold;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #1a8cd8;
    }
    
    /* Links */
    a {
        color: #1d9bf0;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    .contact-btn {
        background-color: #1d9bf0;
        color: white;
        padding: 12px 24px;
        border-radius: 24px;
        text-align: center;
        font-weight: bold;
        display: inline-block;
        margin-top: 20px;
        border: none;
        text-decoration: none;
    }
    
    .contact-btn:hover {
        background-color: #1a8cd8;
        text-decoration: none;
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
        
        .profile-info {
            padding: 12px 16px;
        }
        
        .profile-name {
            font-size: 20px;
        }
        
        .profile-handle {
            font-size: 14px;
        }
        
        .profile-bio {
            font-size: 14px;
            margin-top: 8px;
        }
        
        .profile-meta {
            flex-direction: column;
            gap: 8px;
            font-size: 14px;
        }
        
        .tweet-card {
            border-radius: 0;
            border-left: none;
            border-right: none;
            padding: 12px 16px;
            margin-bottom: 0;
            border-bottom: 1px solid #2f3336;
        }
        
        .tweet-header {
            gap: 10px;
            margin-bottom: 10px;
        }
        
        .tweet-avatar {
            width: 40px;
            height: 40px;
        }
        
        .tweet-name {
            font-size: 15px;
        }
        
        .tweet-handle {
            font-size: 14px;
        }
        
        .tweet-content {
            font-size: 15px;
            margin-bottom: 10px;
        }
        
        .tweet-image {
            border-radius: 12px;
            margin-top: 10px;
        }
        
        .tweet-tags {
            gap: 6px;
            margin-top: 10px;
        }
        
        .tweet-tag {
            padding: 3px 10px;
            font-size: 13px;
        }
        
        .tweet-actions {
            gap: 40px;
            margin-top: 12px;
            padding-top: 10px;
        }
        
        .action-btn {
            font-size: 13px;
            gap: 6px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 12px 0;
            font-size: 14px;
        }
        
        .contact-btn {
            padding: 10px 20px;
            font-size: 15px;
            display: block;
            width: 100%;
        }
        
        /* Make Streamlit columns stack on mobile */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
    }
    
    @media (max-width: 480px) {
        .profile-header {
            height: 120px;
        }
        
        .profile-pic {
            width: 80px;
            height: 80px;
            border: 3px solid #000000;
            margin-top: -40px;
            margin-left: 12px;
        }
        
        .profile-info {
            padding: 10px 12px;
        }
        
        .profile-name {
            font-size: 18px;
        }
        
        .profile-handle {
            font-size: 13px;
        }
        
        .profile-bio {
            font-size: 13px;
        }
        
        .profile-meta {
            font-size: 13px;
        }
        
        .tweet-card {
            padding: 10px 12px;
        }
        
        .tweet-avatar {
            width: 36px;
            height: 36px;
        }
        
        .tweet-name {
            font-size: 14px;
        }
        
        .tweet-handle {
            font-size: 13px;
        }
        
        .tweet-content {
            font-size: 14px;
        }
        
        .tweet-tag {
            padding: 2px 8px;
            font-size: 12px;
        }
        
        .tweet-actions {
            gap: 30px;
        }
        
        .action-btn {
            font-size: 12px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 10px 0;
            font-size: 13px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for likes
if 'likes' not in st.session_state:
    st.session_state.likes = {}

def toggle_like(item_id):
    if item_id not in st.session_state.likes:
        st.session_state.likes[item_id] = False
    st.session_state.likes[item_id] = not st.session_state.likes[item_id]

# Profile Header
st.markdown("""
<div class="profile-header"></div>
<div class="profile-pic"></div>
<div class="profile-info">
    <h1 class="profile-name">Hussein Ali</h1>
    <p class="profile-handle">@husaynali</p>
    <p class="profile-bio">
        BI Developer & Data Analyst 📊 | Computer Science grad specialized in Data | 
        Building impactful Business solutions | Python • SQL • Power BI | 
        Gaming 🎮 • Chess ♟️
    </p>
    <div class="profile-meta">
        <span>📍 Cairo, Egypt</span>
        <span>🔗 <a href="mailto:hire-hussein@proton.me">hire-hussein@proton.me</a></span>
        <span>📅 Joined 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Posts", "💼 Projects", "🛠️ Skills", "📝 Blogs", "📧 Contact"])

with tab1:
    st.markdown("""
    <div class="tweet-card">
        <div class="tweet-header">
            <div class="tweet-avatar"></div>
            <div class="tweet-author">
                <div class="tweet-name">Hussein Ali</div>
                <div class="tweet-handle">@husaynali • now</div>
            </div>
        </div>
        <div class="tweet-content">
            Welcome to my profile! 👋🏽 I'm a BI Developer passionate about transforming raw data into actionable insights. 
            Check out my projects below and let's connect if you're looking to build something amazing together!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("❤️ " + str(st.session_state.likes.get("intro", 0)), key="like_intro"):
            toggle_like("intro")
            st.rerun()

with tab2:
    projects = [
        {
            "id": "project1",
            "name": "Showgeist",
            "description": "A data-driven Streamlit web app offering interactive TV show analytics. Dive into trends, episode-level stats, genre dynamics, and viewing patterns — all in a clean, interactive interface.",
            "tags": ["Python", "Streamlit", "Pandas", "Plotly", "Data Analysis", "API"],
            "links": ["🔗 Live App", "💻 GitHub"],
            "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=400&fit=crop"
        },
        {
            "id": "project2",
            "name": "Supermarket Sales Analysis",
            "description": "A data analytics project that explores supermarket sales data using Python. The analysis uncovers key insights on branch performance, customer demographics, product line revenue, and payment methods.",
            "tags": ["Python", "Pandas", "Matplotlib", "Seaborn", "EDA"],
            "links": ["💻 GitHub"],
            "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=400&fit=crop"
        },
        {
            "id": "project3",
            "name": "Healthcare Operations Dashboard",
            "description": "A detailed Power BI dashboard to monitor and optimize U.S. healthcare operations (2019–2020). Tracks patient growth, CPT units, medical expenses, payer performance, and revenue trends.",
            "tags": ["Power BI", "SQL", "Excel", "DAX", "Data Visualization"],
            "links": ["📊 View Dashboard"],
            "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=400&fit=crop"
        },
        {
            "id": "project4",
            "name": "SCHEDULIZER",
            "description": "A Python package for simulating and visualizing classic CPU scheduling algorithms like FCFS, SJF, Priority, and Round Robin. Designed for educational use with interactive examples.",
            "tags": ["Python", "Educational Tools", "CLI", "PyPI Package"],
            "links": ["💻 GitHub", "📦 PyPI"],
            "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800&h=400&fit=crop"
        }
    ]
    
    for project in projects:
        likes_count = st.session_state.likes.get(project["id"], 0) if st.session_state.likes.get(project["id"]) else 0
        liked_class = "liked" if st.session_state.likes.get(project["id"], False) else ""
        
        st.markdown(f"""
        <div class="tweet-card">
            <div class="tweet-header">
                <div class="tweet-avatar"></div>
                <div class="tweet-author">
                    <div class="tweet-name">Hussein Ali</div>
                    <div class="tweet-handle">@husaynali • Featured Project</div>
                </div>
            </div>
            <div class="tweet-content">
                <strong style="font-size: 18px;">{project['name']}</strong><br>
                {project['description']}
            </div>
            <img src="{project['image']}" class="tweet-image">
            <div class="tweet-tags">
                {''.join([f'<span class="tweet-tag">{tag}</span>' for tag in project['tags']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button(f"{'❤️' if st.session_state.likes.get(project['id'], False) else '🤍'} {likes_count if likes_count > 0 else ''}", key=f"like_{project['id']}"):
                toggle_like(project['id'])
                if st.session_state.likes[project['id']]:
                    if project['id'] not in st.session_state.likes or isinstance(st.session_state.likes[project['id']], bool):
                        st.session_state.likes[project['id']] = 1
                    else:
                        st.session_state.likes[project['id']] += 1
                st.rerun()

with tab3:
    st.markdown("""
    <div class="tweet-card">
        <div class="tweet-header">
            <div class="tweet-avatar"></div>
            <div class="tweet-author">
                <div class="tweet-name">Hussein Ali</div>
                <div class="tweet-handle">@husaynali • Tech Stack</div>
            </div>
        </div>
        <div class="tweet-content">
            <strong style="font-size: 18px;">Technologies I Work With</strong><br><br>
            As a Computer Science graduate with a specialization in Data and a strong passion for Business Intelligence, 
            I enjoy working with data-driven technologies that uncover insights and support smart decision-making.
        </div>
        <div class="tweet-tags">
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
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    blogs = [
        {
            "id": "blog1",
            "title": "The AI Gold Rush: Are We Repeating the Same Mistakes?",
            "description": "A critical look at the current AI boom, exploring how hype-driven decisions echo past tech bubbles. What are we overlooking in our pursuit of innovation?",
            "tags": ["AI Trends", "Tech Ethics", "Strategy"],
            "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=400&fit=crop"
        },
        {
            "id": "blog2",
            "title": "The Two Sum Problem",
            "description": "A beginner-friendly walkthrough of LeetCode's Two Sum problem, covering brute-force, optimized hash-map approaches, and real-world interview tips.",
            "tags": ["Python", "Algorithms", "Problem Solving"],
            "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800&h=400&fit=crop"
        }
    ]
    
    for blog in blogs:
        st.markdown(f"""
        <div class="tweet-card">
            <div class="tweet-header">
                <div class="tweet-avatar"></div>
                <div class="tweet-author">
                    <div class="tweet-name">Hussein Ali</div>
                    <div class="tweet-handle">@husaynali • Blog Post</div>
                </div>
            </div>
            <div class="tweet-content">
                <strong style="font-size: 18px;">{blog['title']}</strong><br>
                {blog['description']}
            </div>
            <img src="{blog['image']}" class="tweet-image">
            <div class="tweet-tags">
                {''.join([f'<span class="tweet-tag">{tag}</span>' for tag in blog['tags']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button(f"🤍", key=f"like_{blog['id']}"):
                toggle_like(blog['id'])
                st.rerun()

with tab5:
    st.markdown("""
    <div class="tweet-card">
        <div class="tweet-header">
            <div class="tweet-avatar"></div>
            <div class="tweet-author">
                <div class="tweet-name">Hussein Ali</div>
                <div class="tweet-handle">@husaynali • Let's Connect</div>
            </div>
        </div>
        <div class="tweet-content">
            <strong style="font-size: 20px;">Have a project or looking to hire?</strong><br><br>
            Feel free to reach out if you're looking to hire, just want to connect, or see if we can build something amazing together.
            <br><br>
            📧 <a href="mailto:hire-hussein@proton.me" style="font-size: 18px;">hire-hussein@proton.me</a>
            <br><br>
            <a href="mailto:hire-hussein@proton.me" class="contact-btn">📩 Get in touch</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 40px 0 20px 0; color: #71767b; border-top: 1px solid #2f3336; margin-top: 40px;">
    © 2026 Hussein Ali • Built with ❤️ (and secretly with Streamlit 🤫)
</div>
""", unsafe_allow_html=True)
