import streamlit as st


def load_theme():
    st.markdown(
        """
        <style>
        body { background-color: #111111; color: #f3f0ff; }
        .stButton>button { background-color: #7c4dff; color: #fff; }
        </style>
        """,
        unsafe_allow_html=True,
    )
