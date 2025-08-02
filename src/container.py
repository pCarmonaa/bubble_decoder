from dependency_injector import containers, providers

from domain.services.atomic_analyzers.emotional_tone_analyzer_service import EmotionalToneAnalyzerService
from domain.services.atomic_analyzers.language_style_analyzer_service import LanguageStyleAnalyzerService
from domain.services.atomic_analyzers.polarization_analyzer_service import PolarizationAnalyzerService
from domain.services.atomic_analyzers.sentiment_analyzer_service import SentimentAnalyzerService
from domain.services.atomic_analyzers.topic_analyzer_service import TopicAnalyzerService
from domain.services.bubble_map_analyzer_service import BubbleMapAnalyzerService

from infrastructure.driven.llm_emotional_analyzer import LlmEmotionalAnalyzer
from infrastructure.driving.content_analyzer_adapter import ContentAnalyzerAdapter

from infrastructure.web.bubble_decoder_api import BubbleDecoderAPI

class Container(containers.DeclarativeContainer):
    llm_emotional_analyzer = providers.Singleton(LlmEmotionalAnalyzer)
    
    emotional_tone_analyzer = providers.Singleton(
        EmotionalToneAnalyzerService, 
        external_emotional_analyzer=llm_emotional_analyzer
    )
    language_style_analyzer = providers.Singleton(LanguageStyleAnalyzerService)
    polarization_analyzer = providers.Singleton(PolarizationAnalyzerService)
    sentiment_analyzer = providers.Singleton(SentimentAnalyzerService)
    topic_analyzer = providers.Singleton(TopicAnalyzerService)
    
    bubble_map_analyzer = providers.Singleton(
        BubbleMapAnalyzerService,
        emotional_tone_analyzer=emotional_tone_analyzer,
        language_style_analyzer=language_style_analyzer,
        polarization_analyzer=polarization_analyzer,
        sentiment_analyzer=sentiment_analyzer,
        topic_analyzer=topic_analyzer
    )
    
    content_analyzer = providers.Singleton(
        ContentAnalyzerAdapter, 
        bubble_map_analyzer=bubble_map_analyzer)
    
    bubble_decoder_api = providers.Singleton(
        BubbleDecoderAPI,
        content_analyzer=content_analyzer
    )