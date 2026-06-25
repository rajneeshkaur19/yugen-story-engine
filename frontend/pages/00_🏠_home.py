import streamlit as st

from frontend.components.story_header import story_header
from frontend.components.story_settings import story_settings
from frontend.components.story_display import story_display


def app():
    st.title("Yugen Story Engine")
    story_header()
    story_settings()
    story_display()
