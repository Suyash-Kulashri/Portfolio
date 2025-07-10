import streamlit as st
from portfolio.header import render_header
from portfolio.hero import render_hero
from portfolio.about import render_about
from portfolio.skills import render_skills
from portfolio.experience import render_experience
from portfolio.projects import render_projects
from portfolio.contact import render_contact
from portfolio.footer import render_footer
from portfolio.styles import render_styles


import sys
sys.dont_write_bytecode = True

st.info("View the Portfolio in light theme for better experience.", icon="ℹ️")

st.set_page_config(
    page_title="Suyash Kulashri - AI/ML Engineer & Data Scientist",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
render_header()

# Render styles (CSS and FontAwesome)
render_styles()

# Main content
#st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Render all sections
render_hero()
render_about()
render_skills()
render_experience()
render_projects()
render_contact()
render_footer()

st.markdown('</div>', unsafe_allow_html=True)
