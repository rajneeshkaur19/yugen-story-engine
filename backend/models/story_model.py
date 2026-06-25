from pydantic import BaseModel
from typing import List, Optional


class StoryRequest(BaseModel):
    prompt: str
    tone: Optional[str] = None
    length: Optional[str] = None
    setting: Optional[str] = None


class StoryResponse(BaseModel):
    id: Optional[int]
    title: str
    content: str
    beats: List[dict]
    tension_curve: dict
    hints: Optional[List[str]] = None
