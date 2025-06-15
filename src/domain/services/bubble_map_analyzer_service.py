from typing import Dict, Any
from domain.ports.driving.atomic_analyzers import (
    EmotionalToneAnalyzer,
    LanguageStyleAnalyzer,
    PolarizationAnalyzer,
    SentimentAnalyzer,
    TopicAnalyzer
)
from domain.ports.driving.bubble_map_analyzer import BubbleMapAnalyzer

class BubbleMapAnalyzerService(BubbleMapAnalyzer):
    def __init__(
            self,
            emotional_tone_analyzer: EmotionalToneAnalyzer,
            language_style_analyzer: LanguageStyleAnalyzer,
            polarization_analyzer: PolarizationAnalyzer,
            sentiment_analyzer: SentimentAnalyzer,
            topic_analyzer: TopicAnalyzer
        ):
        self.emotional_tone_analyzer = emotional_tone_analyzer
        self.language_style_analyzer = language_style_analyzer
        self.polarization_analyzer = polarization_analyzer
        self.sentiment_analyzer = sentiment_analyzer
        self.topic_analyzer = topic_analyzer
    
    def analyze(self, content: str) -> Dict[str, Any]:
        topic_analysis = self.topic_analyzer.analyze(content)
        sentiment_analysis = self.sentiment_analyzer.analyze(content)
        emotional_analysis = self.emotional_tone_analyzer.analyze(content)
        language_analysis = self.language_style_analyzer.analyze(content)
        polarization_analysis = self.polarization_analyzer.analyze(content)
        
        bubble_risk_score = self._calculate_bubble_risk_score(
            sentiment_analysis, 
            emotional_analysis, 
            language_analysis, 
            polarization_analysis
        )
        
        return {
            'content_analysis': {
                'topic': topic_analysis,
                'sentiment': sentiment_analysis,
                'emotional_tone': emotional_analysis,
                'language_style': language_analysis,
                'polarization': polarization_analysis
            },
            'bubble_risk_assessment': {
                'risk_level': self._determine_risk_level(bubble_risk_score),
                'risk_score': bubble_risk_score,
                'risk_factors': self._identify_risk_factors(
                    sentiment_analysis, 
                    emotional_analysis, 
                    language_analysis, 
                    polarization_analysis
                )
            }
        }
    
    def _calculate_bubble_risk_score(self, sentiment_analysis: Dict, emotional_analysis: Dict, 
                                   language_analysis: Dict, polarization_analysis: Dict) -> float:
        risk_factors = []
        
        if sentiment_analysis['polarity_score'] > 0.5 or sentiment_analysis['polarity_score'] < -0.5:
            risk_factors.append(0.2)
        
        if emotional_analysis['emotional_intensity'] > 0.5:
            risk_factors.append(0.2)
        
        if polarization_analysis['polarization_score'] > 0.3:
            risk_factors.append(0.3)
        
        if language_analysis['style'] == 'informal' and polarization_analysis['polarization_score'] > 0.2:
            risk_factors.append(0.1)
        
        return min(1.0, sum(risk_factors))
    
    def _determine_risk_level(self, risk_score: float) -> str:
        if risk_score > 0.6:
            return 'high'
        elif risk_score > 0.3:
            return 'medium'
        else:
            return 'low'
    
    def _identify_risk_factors(self, sentiment_analysis: Dict, emotional_analysis: Dict, 
                             language_analysis: Dict, polarization_analysis: Dict) -> list:
        risk_factors = []
        
        if sentiment_analysis['polarity_score'] > 0.5:
            risk_factors.append('Strong positive bias')
        elif sentiment_analysis['polarity_score'] < -0.5:
            risk_factors.append('Strong negative bias')
        
        if emotional_analysis['emotional_intensity'] > 0.5:
            risk_factors.append('High emotional intensity')
        
        if polarization_analysis['polarization_level'] == 'high':
            risk_factors.append('High polarization')
        
        if language_analysis['style'] == 'informal' and polarization_analysis['polarization_score'] > 0.2:
            risk_factors.append('Informal language with polarizing content')
        
        return risk_factors