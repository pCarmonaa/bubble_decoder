from typing import Dict, Any
from domain.ports.driving.atomic_analyzers import EmotionalToneAnalyzer

class EmotionalToneAnalyzerService(EmotionalToneAnalyzer):
    def analyze(self, content: str) -> Dict[str, Any]:
        content_lower = content.lower()
        
        emotion_keywords = {
            'anger': ['angry', 'furious', 'rage', 'hate', 'outrage', 'frustrated'],
            'joy': ['happy', 'joy', 'excited', 'delighted', 'pleased', 'thrilled'],
            'sadness': ['sad', 'depressed', 'grief', 'sorrow', 'melancholy', 'unhappy'],
            'fear': ['afraid', 'scared', 'terrified', 'anxious', 'worried', 'nervous'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'stunned'],
            'disgust': ['disgusted', 'revolted', 'appalled', 'sickened', 'repulsed']
        }
        
        emotion_scores = {}
        for emotion, keywords in emotion_keywords.items():
            score = sum(content_lower.count(keyword) for keyword in keywords)
            emotion_scores[emotion] = score
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get) if emotion_scores else 'neutral'
        
        return {
            'dominant_emotion': dominant_emotion,
            'emotion_scores': emotion_scores,
            'emotional_intensity': min(1.0, sum(emotion_scores.values()) / len(content.split()) * 5)
        } 