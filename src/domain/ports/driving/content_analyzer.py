from abc import ABC, abstractmethod
from typing import Dict, Any

class ContentAnalyzer(ABC):
    @abstractmethod
    def analyze_bubble_map(self, content: str) -> Dict[str, Any]:
        pass 