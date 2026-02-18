from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class InfographicType(str, Enum):
    timeline = "timeline"
    comparison = "comparison"
    process = "process"
    statistics = "statistics"


class Citation(BaseModel):
    id: int
    title: str
    url: HttpUrl
    publisher: str
    accessed_at: datetime


class LayoutBlock(BaseModel):
    id: str
    type: str
    content: str
    citation_ids: List[int] = []


class InfographicSpec(BaseModel):
    title: str
    generated_at: datetime
    infographic_type: InfographicType
    citations: List[Citation]
    layout_blocks: List[LayoutBlock]
