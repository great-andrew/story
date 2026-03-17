from pydantic import BaseModel
from typing import List


class StoryOutput(BaseModel):

    page: int
    text: str
    visual_prompt: str


class StoryWriterOutput(BaseModel):
    story: List[StoryOutput]
