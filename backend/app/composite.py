from datetime import datetime
from typing import List

from pydantic import BaseModel

from .article import Article
from .spec import InfographicSpec
from .sources import SourceSnapshot


class ResearchSnapshot(BaseModel):
    prompt: str
    generated_at: datetime
    article: Article
    infographic: InfographicSpec
    sources: List[SourceSnapshot]
    confidence_score: float
    ai_generated_label: bool
