import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from domain.models.sentiment.sentiment import Sentiment
from domain.models.sentiment.sentiment_analysis import SentimentAnalysis
from domain.ports.driving.atomic_analyzers import SentimentAnalyzer


class LlmSentimentAnalyzerAdapter(SentimentAnalyzer):
    def __init__(self):
        sentiment_model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
        self.sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
        self.sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)
        
    def analyze(self, text: str) -> SentimentAnalysis:
        sentiment_inputs = self.sentiment_tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            sentiment_outputs = self.sentiment_model(**sentiment_inputs)
            sentiment_scores = torch.nn.functional.softmax(sentiment_outputs.logits, dim=1)
        
        sentiment_scores = {
            Sentiment.NEGATIVE: float(sentiment_scores[0][0]),
            Sentiment.NEUTRAL: float(sentiment_scores[0][1]),
            Sentiment.POSITIVE: float(sentiment_scores[0][2])
        }
        
        return SentimentAnalysis(
            sentiment=max(sentiment_scores, key=sentiment_scores.get), 
            sentiment_scores=sentiment_scores
        )
        