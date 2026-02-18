from collections import OrderedDict
from itertools import count
from typing import Dict, List, Optional

from pydantic import BaseModel

from .composite import ResearchSnapshot


class HistoryEntry(BaseModel):
    id: int
    prompt: str
    version: int
    parent_id: Optional[int]
    created_at: ResearchSnapshot
    snapshot: ResearchSnapshot


class ResearchHistory:
    def __init__(self) -> None:
        self._entries: Dict[int, HistoryEntry] = OrderedDict()
        self._counter = count(1)

    def add(self, prompt: str, snapshot: ResearchSnapshot, parent_id: Optional[int] = None) -> HistoryEntry:
        entry_id = next(self._counter)
        version = 1
        if parent_id:
            parent = self._entries[parent_id]
            version = parent.version + 1
        entry = HistoryEntry(
            id=entry_id,
            prompt=prompt,
            version=version,
            parent_id=parent_id,
            created_at=snapshot,
            snapshot=snapshot,
        )
        self._entries[entry_id] = entry
        return entry

    def get(self, entry_id: int) -> HistoryEntry:
        return self._entries[entry_id]

    def list(self) -> List[HistoryEntry]:
        return list(self._entries.values())
