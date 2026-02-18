from datetime import datetime
from typing import List

from .sources import SourceMetadata, SourceSnapshot


class SourcesService:
    @staticmethod
    def gather_sources(prompt: str) -> List[SourceSnapshot]:
        # Placeholder for real search/fetch logic
        return SourceSnapshot.construct(
            id=1,
            source=SourceMetadata(
                title=f"Placeholder source for '{prompt}'",
                url="https://example.com/placeholder",
                publisher="Example Publisher",
                publish_date=datetime.utcnow(),
                accessed_at=datetime.utcnow(),
                summary="Key claims derived from placeholder data.",
                reliability_score=0.85,
            ),
            snippet="Claim summary for placeholder source.",
        ),
