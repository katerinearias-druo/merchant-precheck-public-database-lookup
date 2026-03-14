from __future__ import annotations

from abc import ABC, abstractmethod

from app.models.schemas import LookupResponse


class BaseLookupService(ABC):
    @abstractmethod
    async def lookup(self, tax_id: str) -> LookupResponse:
        ...
