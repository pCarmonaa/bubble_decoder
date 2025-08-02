from typing import Dict
from domain.ports.driven.external_emotional_analyzer import ExternalEmotionalAnalyzer
from domain.ports.driving.atomic_analyzers import EmotionalToneAnalyzer
from domain.models.emotion.emotion_data import EmotionData
from domain.models.emotion.emotional_analysis import EmotionalAnalysis

class EmotionalToneAnalyzerService(EmotionalToneAnalyzer):
    def __init__(self, external_emotional_analyzer: ExternalEmotionalAnalyzer):
        self.external_emotional_analyzer = external_emotional_analyzer
        self.emotion_weights = EmotionData.WEIGHTS
        self.emotion_categories = EmotionData.CATEGORIES
        
    def _calculate_emotional_intensity(self, emotion_scores: Dict[str, float]) -> float:
        weighted_scores = []
        for emotion, score in emotion_scores.items():
            weight = self.emotion_weights.get(emotion.lower(), 1.0)
            weighted_scores.append(score * weight)
        
        max_weighted_score = max(weighted_scores) if weighted_scores else 0
        return min(1.0, max_weighted_score * 1.2)

    def _calculate_main_emotion_scores(self, emotion_scores: Dict[str, float]) -> Dict[str, float]:
        main_emotion_scores = {}
        for category, emotions in self.emotion_categories.items():
            category_scores = [
                emotion_scores.get(emotion, 0) * self.emotion_weights.get(emotion.lower(), 1.0)
                for emotion in emotions
            ]
            if category_scores:
                category_score = sum(category_scores) / len(category_scores)
                if(category_score >= 0.01):
                    main_emotion_scores[category] = category_score
                    
        return main_emotion_scores

    def _determine_dominant_emotion(self, main_emotion_scores: Dict[str, float]) -> str:
        if not main_emotion_scores:
            return 'neutral'
        return max(main_emotion_scores.items(), key=lambda x: x[1])[0]
    
    def analyze(self, content: str) -> EmotionalAnalysis:
        emotion_scores = self.external_emotional_analyzer.get_emotional_analysis(content)
                
        main_emotion_scores = self._calculate_main_emotion_scores(emotion_scores)
        emotional_intensity = self._calculate_emotional_intensity(emotion_scores)
        dominant_emotion = self._determine_dominant_emotion(main_emotion_scores)

        return EmotionalAnalysis(
            dominant_emotion=dominant_emotion,
            emotion_scores=main_emotion_scores,
            emotional_intensity=emotional_intensity
        ) 