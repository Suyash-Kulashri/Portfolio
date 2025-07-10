import streamlit as st

def render_footer():
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