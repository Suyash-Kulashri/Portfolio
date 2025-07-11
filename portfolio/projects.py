import streamlit as st

def render_projects():
    st.markdown('<section id="projects" style="padding: 80px 0; background: none;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Featured Projects</div><div class="section-divider"></div><div class="section-text">A showcase of my recent work and personal projects that demonstrate my skills and passion for development</div>', unsafe_allow_html=True)
    st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
    projects = [
    {"title": "AI-Powered Text Extractor", "description": "Developed a Python-based application using PyPDF2 and LangChain to extract and organize text from multiple PDFs into structured sections like 'description' and 'key features', saving results in text files.", "image": "📄", "technologies": ["Python", "PyPDF2", "LangChain", "Streamlit", "LLM"], "liveDemo": "#", "github": "#", "color": "from-blue-500 to-cyan-500"},
    {"title": "Machine Learning Model for Financial Forecasting", "description": "Built a machine learning model to perform required return calculations, achieving valuation accuracy within 8% of real-time market prices, utilizing Python and business statistics techniques.", "image": "💹", "technologies": ["Pandas", "Scikit-learn", "Plotly", "Yahoo-Finance","Business Statistics"], "liveDemo": "#", "github": "#", "color": "from-purple-500 to-pink-500"},
    {"title": "Generative AI Chatbot", "description": "Created a generative AI chatbot using Large Language Models and Django, enabling natural language interactions and integrated with cloud services for scalability.", "image": "🤖", "technologies": ["Python", "Django", "Generative AI", "LLMs", "Langchain", "AWS"], "liveDemo": "#", "github": "#", "color": "from-green-500 to-teal-500"},
    {"title": "Deep Learning Image Classifier", "description": "Designed a deep learning model for image classification, trained using TensorFlow, and visualized results with Power BI, enhancing proficiency in neural networks.", "image": "🖼️", "technologies": ["Python", "TensorFlow", "Deep Learning", "Power BI", "NumPy"], "liveDemo": "#", "github": "#", "color": "from-orange-500 to-red-500"},
    {"title": "Data Visualization Dashboard", "description": "Developed an interactive dashboard using Tableau and SQL to analyze time series data, providing insights into trends and patterns for business decision-making.", "image": "📊", "technologies": ["Tableau", "SQL", "Python", "Time Series Analysis", "Pandas"], "liveDemo": "#", "github": "#", "color": "from-indigo-500 to-purple-500"},
    {"title": "Cloud-Based ML Deployment", "description": "Developed and deployed a machine learning model on AWS, optimizing for scalability and integrating with APIs for real-time predictions.", "image": "☁️", "technologies": ["Python", "Scikit-learn", "AWS", "Sagemaker","Databricks", "REST APIs"], "liveDemo": "#", "github": "#", "color": "from-yellow-500 to-orange-500"}
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