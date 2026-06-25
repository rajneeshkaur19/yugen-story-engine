from backend.models.whisper_model import WhisperHint


class WhisperService:
    def generate_hints(self, prompt: str):
        return [
            WhisperHint(theme="Mysterious Echo", hint="A distant bell tolls from a hidden shrine.").dict(),
            WhisperHint(theme="Subtle Tension", hint="The air thickens as a secret is nearly revealed.").dict(),
        ]
