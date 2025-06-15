from typing import Dict, Any
from textblob import TextBlob
from domain.ports.driving.atomic_analyzers import SentimentAnalyzer

class SentimentAnalyzerService(SentimentAnalyzer):
    def analyze(self, content: str) -> Dict[str, Any]:
        blob = TextBlob(content)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0.1:
            sentiment = 'positive'
        elif sentiment_score < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'polarity_score': sentiment_score,
            'subjectivity': blob.sentiment.subjectivity
        } 