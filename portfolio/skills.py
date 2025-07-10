import streamlit as st

def render_skills():
    st.markdown('<section id="skills" style="padding: 80px 0; background: none;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Skills & Expertise</div><div class="section-divider"></div><div class="section-text">A comprehensive toolkit of modern technologies and frameworks I use to bring ideas to life</div>', unsafe_allow_html=True)
    st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
    skill_categories = [
        ("Frontend", "fas fa-code", "from-blue-500 to-cyan-500", ["React", "TypeScript", "Next.js", "Tailwind CSS", "HTML", "Angular", "Streamlit"]),
        ("Backend", "fas fa-database", "from-purple-500 to-pink-500", ["Node.js", "Python", "PostgreSQL", "MongoDB", "Vector Databases (Chroma, Pinecone etc.)", "REST APIs"]),
        ("Tools", "fas fa-tools", "from-green-500 to-teal-500", ["Git", "Docker", "AWS", "Azure", "Databricks", "Streamlit", "Langchain", "AutoGen"])
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
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; max-width: 100%;"> <!-- Added max-width -->
                        {''.join(f'<span style="padding: 4px 12px; background: #f3f4f6; color: #374151; border-radius: 9999px; font-size: 0.875rem; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{skill}</span>' for skill in skills)}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("""
        <div class="card" style="margin-top: 4rem;">
            <h3 style="font-size: 1.5rem; font-weight: bold; text-align: center; color: #1f2937; margin-bottom: 2rem;">Technical Proficiency</h3>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; padding: 0 16px; max-width: 100%;"> <!-- Ensured two-column layout -->
    """, unsafe_allow_html=True)
    proficiencies = [
        ("JavaScript/TypeScript", 60), ("React/Next.js", 60), ("Langchain and AutoGen", 80),
        ("Streamlit", 95), ("Data Science", 85)
    ]
    for name, level in proficiencies:
        st.markdown(f"""
            <div style="margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 500; color: #374151; white-space: nowrap;">{name}</span>
                    <span style="font-size: 0.875rem; color: #6b7280;">{level}%</span>
                </div>
                <div style="width: 100%; background: #e5e7eb; border-radius: 9999px; height: 8px;">
                    <div style="width: {level}%; background: linear-gradient(to right, #2563eb, #7c3aed); height: 8px; border-radius: 9999px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div></div></div></section>', unsafe_allow_html=True)