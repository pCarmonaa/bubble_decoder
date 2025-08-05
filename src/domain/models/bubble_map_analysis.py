from typing import List
from domain.models.topic_analysis import TopicAnalysis
from domain.models.sentiment.sentiment_analysis import SentimentAnalysis
from domain.models.emotion.emotional_analysis import EmotionalAnalysis
from domain.models.language_style_analysis import LanguageStyleAnalysis
from domain.models.polarization_analysis import PolarizationAnalysis

class ContentAnalysis:
    def __init__(self, topic: TopicAnalysis, sentiment: SentimentAnalysis,
                 emotional_tone: EmotionalAnalysis, language_style: LanguageStyleAnalysis, 
                 polarization: PolarizationAnalysis):
        self.topic = topic
        self.sentiment = sentiment
        self.emotional_tone = emotional_tone
        self.language_style = language_style
        self.polarization = polarization

class BubbleRiskAssessment:
    def __init__(self, risk_level: str, risk_score: float, risk_factors: List[str]):
        self.risk_level = risk_level
        self.risk_score = risk_score
        self.risk_factors = risk_factors

class BubbleMapAnalysis:
    def __init__(self, content_analysis: ContentAnalysis, bubble_risk_assessment: BubbleRiskAssessment):
        self.content_analysis = content_analysis
        self.bubble_risk_assessment = bubble_risk_assessment 