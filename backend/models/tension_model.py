from pydantic import BaseModel
from typing import List


class Beat(BaseModel):
    title: str
    description: str
    tension: float


class TensionCurve(BaseModel):
    beats: List[Beat]
