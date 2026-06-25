from backend.services.whisper_service import WhisperService


def test_whisper_hints_generated():
    service = WhisperService()
    hints = service.generate_hints("A hidden library")
    assert isinstance(hints, list)
    assert len(hints) > 0
