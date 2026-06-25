from backend.services.story_engine import StoryEngine


def test_story_engine_returns_story():
    engine = StoryEngine(claude_api_key="")
    story = engine.create_story("A misty train station")
    assert story["title"] == "Untitled Yugen Tale"
    assert "content" in story
