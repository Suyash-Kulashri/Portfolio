import streamlit as st

def render_header():
    st.markdown('<div class="fixed-header">', unsafe_allow_html=True)
    header_cols = st.columns([14, 8])  # Maintain the left-right layout
    with header_cols[0]:
        st.markdown('<div style="font-size: 1.5rem; font-weight: bold; background: linear-gradient(to right, #2563eb, #7c3aed); -webkit-background-clip: text; background-clip: text; color: transparent;">Portfolio</div>', unsafe_allow_html=True)
    with header_cols[1]:
        nav_cols = st.columns(5)
        sections = ['About', 'Skills', 'Experience', 'Projects', 'Contact']
        for idx, section in enumerate(sections):
            with nav_cols[idx]:
                if st.button(section, key=f"nav_{section.lower()}"):
                    # Enhanced JavaScript for smooth scrolling with fallback, delay, and offset
                    st.markdown(f'''
                        <script>
                            setTimeout(function() {{
                                var element = document.getElementById("{section.lower()}");
                                if (element) {{
                                    var headerOffset = 80; // Adjust based on fixed header height
                                    var elementPosition = element.getBoundingClientRect().top + window.scrollY;
                                    var offsetPosition = elementPosition - headerOffset;

                                    window.scrollTo({{ top: offsetPosition, behavior: "smooth" }});
                                }} else {{
                                    console.log("Element {section.lower()} not found, current scrollY: " + window.scrollY);
                                }}
                            }}, 200); // Increased delay to 200ms
                        </script>
                    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)