import streamlit as st
#import streamlit_antd_components as sac # type: ignore

# Inject custom CSS for styling and fixed header
st.markdown("""
    <style>
    /* Fixed Header */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(to right, #ffffffcc, #ffffffcc);
        backdrop-filter: blur(8px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        padding: 10px 20px;
    }
    .fixed-header .stButton > button {
        background: none;
        border: none;
        color: #374151;
        font-size: 16px;
        font-weight: 500;
        padding: 8px 16px;
        transition: color 0.2s;
    }
    .fixed-header .stButton > button:hover {
        color: #2563eb;
    }
    /* Main Content */
    .main-content {
        padding-top: 80px;
    }
    /* Section Styling */
    .section-title {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(to right, #2563eb, #7c3aed);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-divider {
        width: 96px;
        height: 4px;
        background: linear-gradient(to right, #2563eb, #7c3aed);
        border-radius: 9999px;
        margin: 0 auto 1.5rem;
    }
    .section-text {
        font-size: 1.25rem;
        color: #4b5563;
        text-align: center;
        max-width: 768px;
        margin: 0 auto;
    }
    /* Card Styling */
    .card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    /* Button Styling */
    .gradient-button {
        background: linear-gradient(to right, #2563eb, #7c3aed);
        color: white !important;
        border-radius: 9999px;
        padding: 12px 24px;
        font-weight: 600;
        text-align: center;
        display: inline-block;
        transition: transform 0.3s;
    }
    .gradient-button:hover {
        transform: scale(1.05);
    }
    .outline-button {
        border: 2px solid #d1d5db;
        color: #374151 !important;
        border-radius: 9999px;
        padding: 12px 24px;
        font-weight: 600;
        text-align: center;
        display: inline-block;
        transition: border-color 0.2s, color 0.2s;
    }
    .outline-button:hover {
        border-color: #2563eb;
        color: #2563eb !important;
    }
    /* Responsive Design */
    @media (max-width: 768px) {
        .section-title {
            font-size: 2rem;
        }
        .fixed-header .stButton > button {
            font-size: 14px;
            padding: 6px 12px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Fixed Header
st.markdown('<div class="fixed-header">', unsafe_allow_html=True)
header_cols = st.columns([2, 5])
with header_cols[0]:
    st.markdown('<div style="font-size: 1.5rem; font-weight: bold; background: linear-gradient(to right, #2563eb, #7c3aed); -webkit-background-clip: text; background-clip: text; color: transparent;">Portfolio</div>', unsafe_allow_html=True)
with header_cols[1]:
    nav_cols = st.columns(5)
    sections = ['About', 'Skills', 'Experience', 'Projects', 'Contact']
    for idx, section in enumerate(sections):
        with nav_cols[idx]:
            if st.button(section, key=f"nav_{section.lower()}"):
                st.markdown(f'<script>document.getElementById("{section.lower()}").scrollIntoView({{behavior: "smooth"}});</script>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Main Content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Hero Section
st.markdown('<section id="hero">', unsafe_allow_html=True)
st.markdown("""
    <div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(to bottom right, #eff6ff, #f5f3ff); position: relative; overflow: hidden;">
        <div style="position: absolute; top: 80px; left: 80px; width: 288px; height: 288px; background: #bfdbfe; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
        <div style="position: absolute; top: 160px; right: 80px; width: 288px; height: 288px; background: #ddd6fe; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
        <div style="position: absolute; bottom: 80px; left: 160px; width: 288px; height: 288px; background: #fbcfe8; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
        <div style="text-align: center; position: relative; z-index: 10; max-width: 1280px; padding: 24px;">
            <h1 style="font-size: 3rem; font-weight: bold; margin-bottom: 1.5rem; background: linear-gradient(to right, #2563eb, #7c3aed, #db2777); -webkit-background-clip: text; background-clip: text; color: transparent;">
                Suyash Kulashri
            </h1>
            <p style="font-size: 1.5rem; color: #4b5563; margin-bottom: 1rem; font-weight: 300;">
                AI/ML Engineer & Data Scientist
            </p>
            <p style="font-size: 1.125rem; color: #6b7280; margin-bottom: 3rem; max-width: 512px; margin-left: auto; margin-right: auto;">
                Passionate about creating beautiful, functional, and user-centered Gen AI applications. 
                I bring ideas to life through code and design.
            </p>
            <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 4rem;">
                <a href="https://github.com/Suyash-Kulashri" class="gradient-button"><i class="fab fa-github" style="margin-right: 8px;"></i>Github</a>
                <a href="https://www.linkedin.com/in/suyash-kulashri/" class="gradient-button"><i class="fab fa-linkedin" style="margin-right: 8px;"></i>LinkedIn</a>
                <a href="mailto:suyashkulashri12@gmail.com" class="gradient-button"><i class="fas fa-envelope" style="margin-right: 8px;"></i>Email</a>
            </div>
            <div style="display: flex; flex-direction: column; gap: 1rem; align-items: center;">
                <a href="#about" class="gradient-button">Explore My Work</a>
                <a href="#" class="outline-button">Download Resume</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# About Section
st.markdown('<section id="about" style="padding: 80px 0;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div><div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
about_cols = st.columns([1, 1])
with about_cols[0]:
    st.markdown("""
        <div style="position: relative; margin: 0 auto; width: 320px; height: 320px;">
            <div style="position: absolute; inset: 0; background: linear-gradient(to right, #2563eb, #7c3aed); border-radius: 16px; transform: rotate(6deg);"></div>
            <div style="position: absolute; inset: 0; background: #e5e7eb; border-radius: 16px; display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-user" style="font-size: 128px; color: #9ca3af;"></i>
            </div>
        </div>
    """, unsafe_allow_html=True)
with about_cols[1]:
    st.markdown("""
        <div style="margin-bottom: 1.5rem; font-size: 1.125rem; color: #4b5563;">
            Hello! I'm Suyash, a passionate AI/ML Developer and a Data Scientist with over 1 year of experience
            creating Gen AI applications and ML/DL models that make a difference. I specialize in Gen AI
            technologies and have a keen eye for ML and DL.
        </div>
        <div style="font-size: 1.125rem; color: #4b5563;">
            When I'm not coding, you'll find me exploring new technologies, upskilling
            in AI/ML, or enjoying a good cup of coffee while sketching out ideas
            for my next project.
        </div>
    """, unsafe_allow_html=True)
    stats_cols = st.columns(3)
    stats = [("8+", "Projects", "#2563eb"), ("1+", "Years", "#7c3aed"), ("100+", "Cups of Coffee", "#db2777")]
    for idx, (value, label, color) in enumerate(stats):
        with stats_cols[idx]:
            st.markdown(f"""
                <div style="text-align: center; padding: 16px; background: #f9fafb; border-radius: 8px;">
                    <div style="font-size: 1.875rem; font-weight: bold; color: {color}; margin-bottom: 0.5rem;">{value}</div>
                    <div style="color: #4b5563;">{label}</div>
                </div>
            """, unsafe_allow_html=True)
    fun_facts_cols = st.columns(2)
    fun_facts = [
        ("Loves clean code", "fas fa-heart", "#2563eb", "#eff6ff"),
        ("Coffee enthusiast", "fas fa-coffee", "#7c3aed", "#f5f3ff"),
        ("Loves Upskilling", "fas fa-code", "#db2777", "#fce7f3"),
        ("Team player", "fas fa-user", "#10b981", "#ecfdf5")
    ]
    for idx, (text, icon, color, bg_color) in enumerate(fun_facts):
        with fun_facts_cols[idx % 2]:
            st.markdown(f"""
                <div style="display: flex; align-items: center; padding: 16px; background: {bg_color}; border-radius: 8px; margin-top: 1rem;">
                    <i class="{icon}" style="width: 24px; height: 24px; color: {color}; margin-right: 12px;"></i>
                    <span style="color: #374151;">{text}</span>
                </div>
            """, unsafe_allow_html=True)
st.markdown('</div></section>', unsafe_allow_html=True)

# Skills Section
st.markdown('<section id="skills" style="padding: 80px 0; background: #f9fafb;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Skills & Expertise</div><div class="section-divider"></div><div class="section-text">A comprehensive toolkit of modern technologies and frameworks I use to bring ideas to life</div>', unsafe_allow_html=True)
st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
skill_categories = [
    ("Frontend", "fas fa-code", "from-blue-500 to-cyan-500", ["React", "TypeScript", "Next.js", "Tailwind CSS", "Vue.js", "Angular"]),
    ("Backend", "fas fa-database", "from-purple-500 to-pink-500", ["Node.js", "Python", "PostgreSQL", "MongoDB", "REST APIs"]),
    ("Tools", "fas fa-tools", "from-green-500 to-teal-500", ["Git", "Docker", "AWS", "Azure", "Databricks", "Streamlit", "Langchain", "Autogen"])
]
skill_cols = st.columns(3)
for idx, (title, icon, color, skills) in enumerate(skill_categories):
    with skill_cols[idx]:
        st.markdown(f"""
            <div class="card">
                <div style="width: 64px; height: 64px; background: linear-gradient(to right, #3b82f6, #06b6d4); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                    <i class="{icon}" style="color: white; width: 32px; height: 32px;"></i>
                </div>
                <h3 style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 1rem;">{title}</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                    {''.join(f'<span style="padding: 4px 12px; background: #f3f4f6; color: #374151; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;">{skill}</span>' for skill in skills)}
                </div>
            </div>
        """, unsafe_allow_html=True)
st.markdown("""
    <div class="card" style="margin-top: 4rem;">
        <h3 style="font-size: 1.5rem; font-weight: bold; text-align: center; color: #1f2937; margin-bottom: 2rem;">Technical Proficiency</h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;">
""", unsafe_allow_html=True)
proficiencies = [
    ("JavaScript/TypeScript", 60), ("React/Next.js", 60), ("Langchain and AutoGen", 80),
    ("Streamlit", 95), ("Data Science", 85)
]
for name, level in proficiencies:
    st.markdown(f"""
        <div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 500; color: #374151;">{name}</span>
                <span style="font-size: 0.875rem; color: #6b7280;">{level}%</span>
            </div>
            <div style="width: 100%; background: #e5e7eb; border-radius: 9999px; height: 8px;">
                <div style="width: {level}%; background: linear-gradient(to right, #2563eb, #7c3aed); height: 8px; border-radius: 9999px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div></div></div></section>', unsafe_allow_html=True)

# Experience Section
st.markdown('<section id="experience" style="padding: 80px 0;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Work Experience</div><div class="section-divider"></div><div class="section-text">My professional journey and the amazing experiences that shaped my career</div>', unsafe_allow_html=True)
st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown('<div style="position: relative;"><div style="position: absolute; left: 50%; width: 2px; height: 100%; background: linear-gradient(to bottom, #2563eb, #7c3aed); transform: translateX(-50%);"></div></div>', unsafe_allow_html=True)
experiences = [
    {
        "title": "AI/ML Engineer", "company": "JD Fusion", "location": "Dehradun, India", "period": "2025 - Present",
        "description": "Member of a team of 5 developers in building scalable Gen AI applications using Langchain, Autogen, Streamlit and AWS. Improved application performance by 40% and reduced load times by 60%.",
        "achievements": [
            "Architected database design for a large-scale AI application",
            "Implemented advanced AI algorithms for data processing",
            "Collaborated with cross-functional teams to deliver high-quality software solutions"
        ], "color": "from-blue-500 to-cyan-500"
    },
    {
        "title": "Gen AI Engineer", "company": "Infosys", "location": "WFH", "period": "2024 - 2025",
        "description": "Developed and maintained Traffic Sign Prediction System for autonomous vehicles with an emphasis on real-time data processing and model optimization.",
        "achievements": [
            "Built and deployed a real-time traffic sign detection model",
            "Achieved 95% accuracy in traffic sign recognition",
            "Optimized model inference time by 30% using TensorFlow",
            "Integrated third-party APIs"
        ], "color": "from-purple-500 to-pink-500"
    },
    {
        "title": "Gen AI Engineer Intern", "company": "Learner's Galaxy", "location": "Dehradun, India", "period": "2024 - 2024",
        "description": "Developed a Gen AI application for personalized learning experiences using AI-driven recommendations and adaptive learning paths.",
        "achievements": [
            "Developed a personalized learning chatbot using AutoGen",
            "Built Frontend using React and Tailwind CSS",
            "Integrated AI-driven recommendations for personalized learning paths"
        ], "color": "from-green-500 to-teal-500"
    }
]
for idx, exp in enumerate(experiences):
    st.markdown(f"""
        <div style="position: relative; margin-bottom: 48px;">
            <div style="position: absolute; left: 50%; width: 16px; height: 16px; background: linear-gradient(to right, #{exp['color'].split('-')[1][:-3]}, #{exp['color'].split('-')[3][:-3]}); border-radius: 9999px; transform: translateX(-50%); border: 4px solid white; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"></div>
            <div class="card" style="margin-left: {0 if idx % 2 == 0 else 'auto'}; margin-right: {0 if idx % 2 == 1 else 'auto'}; width: 50%;">
                <h3 style="font-size: 1.25rem; font-weight: bold; color: #1f2937; margin-bottom: 0.5rem;">{exp['title']}</h3>
                <div style="display: flex; gap: 16px; color: #4b5563; font-size: 0.875rem; margin-bottom: 0.5rem;">
                    <div><i class="fas fa-building" style="margin-right: 4px;"></i>{exp['company']}</div>
                    <div><i class="fas fa-map-pin" style="margin-right: 4px;"></i>{exp['location']}</div>
                </div>
                <div style="display: flex; gap: 4px; color: #6b7280; font-size: 0.875rem;">
                    <i class="fas fa-calendar" style="margin-right: 4px;"></i>{exp['period']}
                </div>
                <p style="color: #4b5563; margin: 1rem 0;">{exp['description']}</p>
                <div>
                    <h4 style="font-weight: 600; color: #1f2937; font-size: 0.875rem;">Key Achievements:</h4>
                    <ul style="margin-top: 0.5rem;">
                        {''.join(f'<li style="display: flex; align-items: flex-start; color: #4b5563; font-size: 0.875rem;"><div style="width: 8px; height: 8px; background: linear-gradient(to right, #{exp["color"].split("-")[1][:-3]}, #{exp["color"].split("-")[3][:-3]}); border-radius: 9999px; margin: 8px 12px 0 0;"></div>{achievement}</li>' for achievement in exp['achievements'])}
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div></section>', unsafe_allow_html=True)

# Projects Section
st.markdown('<section id="projects" style="padding: 80px 0; background: #f9fafb;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Featured Projects</div><div class="section-divider"></div><div class="section-text">A showcase of my recent work and personal projects that demonstrate my skills and passion for development</div>', unsafe_allow_html=True)
st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
projects = [
    {"title": "E-Commerce Platform", "description": "A full-stack e-commerce platform built with React, Node.js, and PostgreSQL. Features include user authentication, payment processing, and admin dashboard.", "image": "🛒", "technologies": ["React", "Node.js", "PostgreSQL", "Stripe", "Tailwind CSS"], "liveDemo": "#", "github": "#", "color": "from-blue-500 to-cyan-500"},
    {"title": "Task Management App", "description": "A collaborative task management application with real-time updates, drag-and-drop functionality, and team collaboration features.", "image": "📋", "technologies": ["Next.js", "TypeScript", "Socket.io", "MongoDB", "Framer Motion"], "liveDemo": "#", "github": "#", "color": "from-purple-500 to-pink-500"},
    {"title": "Weather Dashboard", "description": "A beautiful weather dashboard with location-based forecasts, interactive maps, and detailed weather analytics.", "image": "🌤️", "technologies": ["Vue.js", "Chart.js", "OpenWeather API", "Mapbox", "SCSS"], "liveDemo": "#", "github": "#", "color": "from-green-500 to-teal-500"},
    {"title": "Social Media App", "description": "A modern social media application with real-time messaging, photo sharing, and social features.", "image": "📱", "technologies": ["React Native", "Firebase", "Redux", "Expo", "Node.js"], "liveDemo": "#", "github": "#", "color": "from-orange-500 to-red-500"},
    {"title": "Portfolio Website", "description": "A responsive portfolio website showcasing my work with smooth animations and modern design principles.", "image": "💼", "technologies": ["React", "Tailwind CSS", "Framer Motion", "Vercel"], "liveDemo": "#", "github": "#", "color": "from-indigo-500 to-purple-500"},
    {"title": "Crypto Tracker", "description": "A cryptocurrency tracking application with real-time price updates, portfolio management, and market analysis.", "image": "₿", "technologies": ["Angular", "TypeScript", "CoinGecko API", "Chart.js", "Bootstrap"], "liveDemo": "#", "github": "#", "color": "from-yellow-500 to-orange-500"}
]
project_cols = st.columns(3)
for idx, project in enumerate(projects):
    with project_cols[idx % 3]:
        st.markdown(f"""
            <div class="card">
                <div style="height: 192px; background: linear-gradient(to bottom right, #{project['color'].split('-')[1][:-3]}, #{project['color'].split('-')[3][:-3]}); display: flex; align-items: center; justify-content: center;">
                    <div style="font-size: 3rem;">{project['image']}</div>
                </div>
                <div style="padding: 24px;">
                    <h3 style="font-size: 1.25rem; font-weight: bold; color: #1f2937; margin-bottom: 0.75rem;">{project['title']}</h3>
                    <p style="color: #4b5563; margin-bottom: 1rem;">{project['description']}</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 1.5rem;">
                        {''.join(f'<span style="padding: 4px 12px; background: #f3f4f6; color: #374151; border-radius: 9999px; font-size: 0.75rem; font-weight: 500;">{tech}</span>' for tech in project['technologies'])}
                    </div>
                    <div style="display: flex; gap: 16px;">
                        <a href="{project['liveDemo']}" class="gradient-button"><i class="fas fa-external-link-alt" style="margin-right: 8px;"></i>Live Demo</a>
                        <a href="{project['github']}" class="outline-button"><i class="fab fa-github" style="margin-right: 8px;"></i>Code</a>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
st.markdown('<div style="text-align: center; margin-top: 3rem;"><a href="#" class="gradient-button">View All Projects</a></div></div></section>', unsafe_allow_html=True)

# Contact Section
st.markdown('<section id="contact" style="padding: 80px 0;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Get In Touch</div><div class="section-divider"></div><div class="section-text">I\'m always interested in new opportunities and exciting projects. Let\'s create something amazing together!</div>', unsafe_allow_html=True)
st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
contact_cols = st.columns(2)
with contact_cols[0]:
    st.markdown("""
        <h3 style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 1.5rem;">Let's Connect</h3>
        <p style="color: #4b5563; margin-bottom: 2rem;">Whether you have a project in mind, want to collaborate, or just want to say hello, I'd love to hear from you. Feel free to reach out through any of these channels.</p>
        <div style="margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px; margin-bottom: 1rem;">
                <div style="width: 48px; height: 48px; background: linear-gradient(to right, #2563eb, #7c3aed); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                    <i class="fas fa-envelope" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div>
                    <h4 style="font-weight: 600; color: #1f2937;">Email</h4>
                    <p style="color: #4b5563;">suyashkulashri12@gmail.com</p>
                </div>
            </div>
            <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px; margin-bottom: 1rem;">
                <div style="width: 48px; height: 48px; background: linear-gradient(to right, #10b981, #14b8a6); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                    <i class="fas fa-phone" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div>
                    <h4 style="font-weight: 600; color: #1f2937;">Phone</h4>
                    <p style="color: #4b5563;">+918439916910</p>
                </div>
            </div>
            <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px;">
                <div style="width: 48px; height: 48px; background: linear-gradient(to right, #f97316, #ef4444); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                    <i class="fas fa-map-pin" style="color: white; width: 24px; height: 24px;"></i>
                </div>
                <div>
                    <h4 style="font-weight: 600; color: #1f2937;">Location</h4>
                    <p style="color: #4b5563;">Dehradun, India</p>
                </div>
            </div>
        </div>
        <div>
            <h4 style="font-weight: 600; color: #1f2937; margin-bottom: 1rem;">Follow Me</h4>
            <div style="display: flex; gap: 16px;">
                <a href="https://github.com/Suyash-Kulashri" class="gradient-button"><i class="fab fa-github" style="margin-right: 8px;"></i>Github</a>
                <a href="https://www.linkedin.com/in/suyash-kulashri/" class="gradient-button"><i class="fab fa-linkedin" style="margin-right: 8px;"></i>LinkedIn</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
with contact_cols[1]:
    with st.form("contact_form"):
        st.markdown('<h3 style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 1.5rem;">Send a Message</h3>', unsafe_allow_html=True)
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Email Address", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Tell me about your project or just say hello!", height=150)
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        if submitted:
            st.write("Message sent! Thank you for reaching out.")
st.markdown('</div></section>', unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <footer style="background: #111827; color: white; padding: 32px 0;">
        <div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">
            <div style="display: flex; flex-direction: column; align-items: center; gap: 16px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #9ca3af;">Made with</span>
                    <i class="fas fa-heart" style="color: #ef4444; width: 16px; height: 16px;"></i>
                    <span style="color: #9ca3af;">by Suyash Kulashri</span>
                </div>
                <div style="color: #9ca3af; font-size: 0.875rem;">
                    © 2025 Suyash Kulashri. All rights reserved.
                </div>
            </div>
        </div>
    </footer>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Load FontAwesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)