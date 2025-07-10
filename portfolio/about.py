import streamlit as st

def render_about():
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