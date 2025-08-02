from abc import ABC, abstractmethod
from domain.models.bubble_map_analysis import BubbleMapAnalysis

class ContentAnalyzer(ABC):
    @abstractmethod
    def analyze_bubble_map(self, content: str) -> BubbleMapAnalysis:
        pass 