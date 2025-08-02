from abc import abstractmethod

from domain.models.emotion.emotional_analysis import EmotionalAnalysis
from domain.models.language_style_analysis import LanguageStyleAnalysis
from domain.models.polarization_analysis import PolarizationAnalysis
from domain.models.sentiment_analysis import SentimentAnalysis
from domain.models.topic_analysis import TopicAnalysis

class EmotionalToneAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> EmotionalAnalysis:
        pass
    
class LanguageStyleAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> LanguageStyleAnalysis:
        pass
    
class PolarizationAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> PolarizationAnalysis:
        pass
    
class SentimentAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> SentimentAnalysis:
        pass
    
class TopicAnalyzer:
    @abstractmethod
    def analyze(self, content: str) -> TopicAnalysis:
        pass