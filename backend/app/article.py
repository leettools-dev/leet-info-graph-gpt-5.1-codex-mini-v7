from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, HttpUrl


class ArticleSection(BaseModel):
    title: str
    content: str
    citations: List[int] = Field(default_factory=list)


class Article(BaseModel):
    prompt: str
    generated_at: datetime
    overview: ArticleSection
    key_points: List[str]
    detailed_explanation: ArticleSection
    implications: ArticleSection
    limitations: ArticleSection
    sources: List[HttpUrl]
    confidence_notes: str
