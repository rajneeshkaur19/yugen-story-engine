import streamlit as st


def top_navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Library", "Settings", "About"])
    return page
