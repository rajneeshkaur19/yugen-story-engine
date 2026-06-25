from backend.services.story_engine import StoryEngine


if __name__ == "__main__":
    engine = StoryEngine(claude_api_key="")
    print(engine.create_story("Sample prompt"))
