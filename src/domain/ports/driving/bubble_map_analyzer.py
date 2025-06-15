from abc import abstractmethod
from typing import Any, Dict

class BubbleMapAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> Dict[str, Any]:
        pass