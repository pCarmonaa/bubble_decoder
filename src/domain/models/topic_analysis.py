from typing import Dict

class TopicAnalysis:
    def __init__(self, primary_topic: str, topic_scores: Dict[str, int], confidence: float):
        self.primary_topic = primary_topic
        self.topic_scores = topic_scores
        self.confidence = confidence 