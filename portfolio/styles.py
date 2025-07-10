import streamlit as st

def render_styles():
    st.markdown("""
        <style>
        /* Fixed Header */
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: #111827;
            backdrop-filter: blur(8px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            z-index: 1000; /* Ensure it stays above other content */
            padding: 10px 20px;
        }
        .fixed-header .stButton > button {
            background: none;
            border: none;
            color: #d1d5db;
            font-size: 16px;
            font-weight: 500;
            padding: 8px 16px;
            transition: color 0.2s;
        }
        .fixed-header .stButton > button:hover {
            color: #93c5fd;
        }
        /* Main Content */
        .main-content {
            padding-top: 80px; /* Adjusted to account for fixed header height */
        }
        /* Section Styling */
        .section-title {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(to right, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-align: center;
            margin-bottom: 1rem;
        }
        .section-divider {
            width: 96px;
            height: 4px;
            background: linear-gradient(to right, #2563eb, #7c3aed);
            border-radius: 9999px;
            margin: 0 auto 1.5rem;
        }
        .section-text {
            font-size: 1.25rem;
            color: #4b5563;
            text-align: center;
            max-width: 768px;
            margin: 0 auto;
        }
        /* Card Styling */
        .card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        /* Button Styling */
        .gradient-button {
            background: linear-gradient(to right, #2563eb, #7c3aed);
            color: white !important;
            border-radius: 9999px;
            padding: 12px 24px;
            font-weight: 600;
            text-align: center;
            display: inline-block;
            transition: transform 0.3s;
        }
        .gradient-button:hover {
            transform: scale(1.05);
        }
        .outline-button {
            border: 2px solid #d1d5db;
            color: #374151 !important;
            border-radius: 9999px;
            padding: 12px 24px;
            font-weight: 600;
            text-align: center;
            display: inline-block;
            transition: border-color 0.2s, color 0.2s;
        }
        .outline-button:hover {
            border-color: #2563eb;
            color: #2563eb !important;
        }
        /* Contact Column Styling */
        .contact-column {
            min-height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        /* Responsive Design */
        @media (max-width: 768px) {
            .section-title {
                font-size: 2rem;
            }
            .fixed-header .stButton > button {
                font-size: 14px;
                padding: 6px 12px;
            }
        }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)