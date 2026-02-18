from typing import List

from .sources import SourceSnapshot, sample_sources


class SourcesService:
    @staticmethod
    def gather_sources(prompt: str) -> List[SourceSnapshot]:
        return sample_sources(prompt)
