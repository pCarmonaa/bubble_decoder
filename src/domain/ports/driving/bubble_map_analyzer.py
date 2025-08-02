from abc import abstractmethod
from domain.models.bubble_map_analysis import BubbleMapAnalysis

class BubbleMapAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> BubbleMapAnalysis:
        pass