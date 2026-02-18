from datetime import datetime
from typing import List

from .article import Article, ArticleSection


class ArticleGenerator:
    @staticmethod
    def create_example(prompt: str, sources: List[str]) -> Article:
        fetched_sources = [f"[{index + 1}] {source}" for index, source in enumerate(sources)]
        overview = ArticleSection(
            title="Overview",
            content=f"This article provides a structured overview of: {prompt}",
            citation_ids=[1],
        )
        detailed_explanation = ArticleSection(
            title="Detailed Explanation",
            content="Detailed insights derived from the fetched sources.",
            citation_ids=[1, 2],
        )
        implications = ArticleSection(
            title="Implications / Applications",
            content="Key implications that stem from this research summary.",
            citation_ids=[2],
        )
        limitations = ArticleSection(
            title="Limitations / Uncertainties",
            content="Known limitations include sourcing freshness and model assumptions.",
            citation_ids=[2, 3],
        )
        return Article(
            prompt=prompt,
            generated_at=datetime.utcnow(),
            overview=overview,
            key_points=[
                "Key point 1 derived from source 1",
                "Key point 2 derived from source 2",
                "Key point 3 highlighting uncertainty",
            ],
            detailed_explanation=detailed_explanation,
            implications=implications,
            limitations=limitations,
            sources=[HttpUrl(source, scheme="https") for source in sources],
            source_ids=list(range(1, len(sources) + 1)),
            confidence_notes="Model confidence is moderate; rely on cited sources.",
        )
