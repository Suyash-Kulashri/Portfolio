import streamlit as st

def render_contact():
    st.markdown('<section id="contact" style="padding: 80px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Get In Touch</div><div class="section-divider"></div><div class="section-text">I\'m always interested in new opportunities and exciting projects. Let\'s create something amazing together!</div>', unsafe_allow_html=True)
    st.markdown('<div class="container" style="max-width: 1280px; padding: 0 24px; margin: 0 auto;">', unsafe_allow_html=True)
    contact_cols = st.columns(2)
    with contact_cols[0]:
        st.markdown('<div class="contact-column" style="padding: 16px;">', unsafe_allow_html=True)
        st.markdown("""
            <h3 style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 1.5rem;">Let's Connect</h3>
            <p style="color: #4b5563; margin-bottom: 2rem;">Whether you have a project in mind, want to collaborate, or just want to say hello, I'd love to hear from you. Feel free to reach out through any of these channels.</p>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px; margin-bottom: 1rem;">
                    <div style="width: 48px; height: 48px; background: linear-gradient(to right, #2563eb, #7c3aed); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                        <i class="fas fa-envelope" style="color: white; width: 15px; height: 15px;"></i>
                    </div>
                    <div>
                        <h4 style="font-weight: 600; color: #1f2937;">Email</h4>
                        <p style="color: #4b5563;">suyashkulashri12@gmail.com</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px; margin-bottom: 1rem;">
                    <div style="width: 48px; height: 48px; background: linear-gradient(to right, #10b981, #14b8a6); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                        <i class="fas fa-phone" style="color: white; width: 15px; height: 15px;"></i>
                    </div>
                    <div>
                        <h4 style="font-weight: 600; color: #1f2937;">Phone</h4>
                        <p style="color: #4b5563;">+918439916910</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; padding: 16px; background: #f9fafb; border-radius: 8px;">
                    <div style="width: 48px; height: 48px; background: linear-gradient(to right, #f97316, #ef4444); border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                        <i class="fas fa-map-pin" style="color: white; width: 15px; height: 15px;"></i>
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
        st.markdown('</div>', unsafe_allow_html=True)  # Close contact-column div
    with contact_cols[1]:
        st.markdown('<div class="contact-column" style="padding: 16px;">', unsafe_allow_html=True)
        with st.form("contact_form"):
            st.markdown('<h3 style="font-size: 1.5rem; font-weight: bold; color: #1f2937; margin-bottom: 1.5rem;">Send a Message</h3>', unsafe_allow_html=True)
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Email Address", placeholder="Enter your email")
            message = st.text_area("Message", placeholder="Tell me about your project or just say hello!", height=150)
            submitted = st.form_submit_button("Send Message", use_container_width=True)
            if submitted:
                st.write("Message sent! Thank you for reaching out.")
        st.markdown('</div>', unsafe_allow_html=True)  # Close contact-column div
    st.markdown('</div></section>', unsafe_allow_html=True)