import streamlit as st

def render_experience():
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