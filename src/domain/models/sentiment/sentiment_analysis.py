from typing import Dict
from domain.models.sentiment.sentiment import Sentiment

class SentimentAnalysis:
    def __init__(self, sentiment: Sentiment, sentiment_scores: Dict[Sentiment, float]):
        self.sentiment = sentiment
        self.sentiment_scores = sentiment_scores