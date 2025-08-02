class SentimentAnalysis:
    def __init__(self, sentiment: str, polarity_score: float, subjectivity: float):
        self.sentiment = sentiment
        self.polarity_score = polarity_score
        self.subjectivity = subjectivity 