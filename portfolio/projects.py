import streamlit as st

def render_projects():
    st.markdown('<section id="projects" style="padding: 80px 0; background: none;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Featured Projects</div><div class="section-divider"></div><div class="section-text">A showcase of my recent work and personal projects that demonstrate my skills and passion for development</div>', unsafe_allow_html=True)
    st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
    projects = [
        {"title": "E-Commerce Platform", "description": "A full-stack e-commerce platform with features like user authentication, payment processing, and admin dashboard.", "image": "🛒", "technologies": ["React", "Node.js", "PostgreSQL", "Stripe", "Tailwind CSS"], "liveDemo": "#", "github": "#", "color": "from-blue-500 to-cyan-500"},
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