from typing import Dict

class EmotionalAnalysis:
    def __init__(self, dominant_emotion: str, emotion_scores: Dict[str, float],
                 emotional_intensity: float):
        self.dominant_emotion = dominant_emotion
        self.emotion_scores = emotion_scores
        self.emotional_intensity = emotional_intensity 