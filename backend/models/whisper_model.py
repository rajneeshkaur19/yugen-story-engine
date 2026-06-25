from pydantic import BaseModel
from typing import List, Optional


class WhisperHint(BaseModel):
    theme: str
    hint: str
    mood: Optional[str] = None
    vibe: Optional[str] = None
    tags: Optional[List[str]] = None
