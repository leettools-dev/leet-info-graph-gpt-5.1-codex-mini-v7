from dataclasses import dataclass
from datetime import datetime
from threading import Lock
from typing import Dict, Set

from pydantic import BaseModel


@dataclass
class UserPromptInfo:
    first_prompt_at: datetime


class ActivationReport(BaseModel):
    total_users: int
    activated_users: int
    activation_rate: float
    last_updated: datetime


class ActivationMetrics:
    def __init__(self) -> None:
        self._lock = Lock()
        self._user_prompts: Dict[str, UserPromptInfo] = {}
        self._sign_ins: Set[str] = set()
        self._last_updated = datetime.utcnow()

    def register_sign_in(self, user_id: str) -> None:
        with self._lock:
            if user_id not in self._sign_ins:
                self._sign_ins.add(user_id)
                self._update_timestamp()

    def register_prompt(self, user_id: str) -> None:
        with self._lock:
            self.register_sign_in(user_id)
            if user_id not in self._user_prompts:
                self._user_prompts[user_id] = UserPromptInfo(first_prompt_at=datetime.utcnow())
                self._update_timestamp()

    def _update_timestamp(self) -> None:
        self._last_updated = datetime.utcnow()

    def report(self) -> ActivationReport:
        total_users = len(self._sign_ins)
        activated_users = len(self._user_prompts)
        activation_rate = (activated_users / total_users) if total_users else 0.0
        return ActivationReport(
            total_users=total_users,
            activated_users=activated_users,
            activation_rate=round(activation_rate, 4),
            last_updated=self._last_updated,
        )


action_metrics = ActivationMetrics()
