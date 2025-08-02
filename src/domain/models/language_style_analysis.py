class LanguageStyleAnalysis:
    def __init__(self, style: str, avg_sentence_length: float, avg_word_length: float,
                 formal_score: int, informal_score: int):
        self.style = style
        self.avg_sentence_length = avg_sentence_length
        self.avg_word_length = avg_word_length
        self.formal_score = formal_score
        self.informal_score = informal_score 