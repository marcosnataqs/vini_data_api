from abc import ABC, abstractmethod
from typing import Any, List

from pydantic import BaseModel


class BaseExtraction(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def extract(self, year: int) -> BaseModel:
        pass

    @abstractmethod
    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        pass
