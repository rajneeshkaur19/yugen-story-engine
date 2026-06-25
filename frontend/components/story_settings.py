import streamlit as st


def story_settings():
    st.sidebar.header("Story Settings")
    tone = st.sidebar.selectbox("Tone", ["mysterious", "melancholic", "celestial", "tense", "dreamy"])
    length = st.sidebar.selectbox("Length", ["short", "medium", "long"])
    setting = st.sidebar.selectbox("Setting", ["shrine", "school", "station", "hospital", "library"])
    return tone, length, setting
