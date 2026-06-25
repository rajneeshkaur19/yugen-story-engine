from backend.services.claude_service import ClaudeService
from backend.services.whisper_service import WhisperService
from backend.services.restraint_filter import RestraintFilter


class StoryEngine:
    def __init__(self, claude_api_key: str):
        self.claude = ClaudeService(claude_api_key)
        self.filter = RestraintFilter()
        self.whisper = WhisperService()

    def create_story(self, prompt: str) -> dict:
        story_text = self.claude.generate_story(prompt)
        return {
            "title": "Untitled Yugen Tale",
            "content": story_text,
            "beats": [],
            "tension_curve": {},
            "hints": self.whisper.generate_hints(prompt),
        }
