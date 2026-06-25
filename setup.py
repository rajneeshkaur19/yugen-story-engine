from setuptools import setup, find_packages

setup(
    name="yugen-story-engine",
    version="0.1.0",
    packages=find_packages(include=["backend*", "frontend*", "tests*"]),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "sqlalchemy",
        "streamlit",
    ],
)
