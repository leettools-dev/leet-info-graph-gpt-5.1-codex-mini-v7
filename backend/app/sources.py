from datetime import datetime
from typing import List

from pydantic import BaseModel, HttpUrl


class SourceMetadata(BaseModel):
    title: str
    url: HttpUrl
    publisher: str
    publish_date: datetime
    accessed_at: datetime
    summary: str
    reliability_score: float


class SourceSnapshot(BaseModel):
    id: int
    source: SourceMetadata
    snippet: str


def sample_sources(prompt: str) -> List[SourceSnapshot]:
    now = datetime.utcnow()
    base_url = "https://example.com/research"
    return [
        SourceSnapshot(
            id=index + 1,
            source=SourceMetadata(
                title=f"{prompt} Insight {index + 1}",
                url=HttpUrl(f"{base_url}/article-{index + 1}", scheme="https"),
                publisher="Example Publisher",
                publish_date=now,
                accessed_at=now,
                summary=f"Summary point {index + 1} derived from data about {prompt}.",
                reliability_score=round(0.92 - (index * 0.1), 2),
            ),
            snippet=f"Key claim {index + 1} for {prompt}.",
        )
        for index in range(3)
    ]
