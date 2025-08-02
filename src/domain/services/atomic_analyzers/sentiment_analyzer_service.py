from textblob import TextBlob
from domain.ports.driving.atomic_analyzers import SentimentAnalyzer
from domain.models.sentiment_analysis import SentimentAnalysis

class SentimentAnalyzerService(SentimentAnalyzer):
    def analyze(self, content: str) -> SentimentAnalysis:
        blob = TextBlob(content)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0.1:
            sentiment = 'positive'
        elif sentiment_score < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return SentimentAnalysis(
            sentiment=sentiment,
            polarity_score=sentiment_score,
            subjectivity=blob.sentiment.subjectivity
        ) 