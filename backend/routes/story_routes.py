from fastapi import APIRouter
from backend.models.story_model import StoryRequest, StoryResponse
from backend.services.story_engine import StoryEngine

router = APIRouter(prefix="/story", tags=["story"])

story_engine = StoryEngine(claude_api_key="")

@router.post("/generate", response_model=StoryResponse)
def generate_story(request: StoryRequest):
    story = story_engine.create_story(request.prompt)
    return StoryResponse(**story)
