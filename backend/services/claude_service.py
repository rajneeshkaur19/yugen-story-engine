import os


class ClaudeService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_story(self, prompt: str) -> str:
        return f"Generated story based on: {prompt}"
