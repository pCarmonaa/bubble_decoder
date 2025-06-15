from typing import Any, Dict
from domain.ports.driving.content_analyzer import ContentAnalyzer
from domain.services.bubble_map_analyzer_service import BubbleMapAnalyzer

class ContentAnalyzerAdapter(ContentAnalyzer):
    def __init__(self, bubble_map_analyzer: BubbleMapAnalyzer):
        self.bubble_map_analyzer = bubble_map_analyzer
        
    
    def analyze_bubble_map(self, content: str) -> Dict[str, Any]:
        return self.bubble_map_analyzer.analyze(content)