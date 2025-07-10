import streamlit as st

def render_hero():
    st.markdown('<section id="hero">', unsafe_allow_html=True)
    st.markdown("""
        <div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(to bottom right, #eff6ff, #f5f3ff); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 80px; left: 80px; width: 288px; height: 288px; background: #bfdbfe; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
            <div style="position: absolute; top: 160px; right: 80px; width: 288px; height: 288px; background: #ddd6fe; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
            <div style="position: absolute; bottom: 80px; left: 160px; width: 288px; height: 288px; background: #fbcfe8; border-radius: 9999px; filter: blur(72px); opacity: 0.3;"></div>
            <div style="text-align: center; position: relative; z-index: 10; max-width: 1280px; padding: 24px;">
                <h1 style="font-size: 5rem; font-weight: bold; margin-bottom: 1.5rem; background: linear-gradient(to right, #2563eb, #7c3aed, #db2777); -webkit-background-clip: text; background-clip: text; color: transparent;">
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
                <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 3rem;">
                    <a href="#about" class="gradient-button">Explore My Work</a>
                    <a href="#" class="outline-button">Download Resume</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</section>', unsafe_allow_html=True)