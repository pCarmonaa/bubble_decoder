from nltk.tokenize import word_tokenize
from domain.ports.driving.atomic_analyzers import LanguageStyleAnalyzer
from domain.models.language_style_analysis import LanguageStyleAnalysis

class LanguageStyleAnalyzerService(LanguageStyleAnalyzer):
    def analyze(self, content: str) -> LanguageStyleAnalysis:
        words = word_tokenize(content)
        sentences = content.split('.')
        
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        
        formal_indicators = ['therefore', 'however', 'furthermore', 'consequently', 'nevertheless']
        informal_indicators = ['lol', 'omg', 'wtf', 'awesome', 'cool', 'dude']
        
        formal_score = sum(content.lower().count(indicator) for indicator in formal_indicators)
        informal_score = sum(content.lower().count(indicator) for indicator in informal_indicators)
        
        if formal_score > informal_score:
            style = 'formal'
        elif informal_score > formal_score:
            style = 'informal'
        else:
            style = 'neutral'
        
        return LanguageStyleAnalysis(
            style=style,
            avg_sentence_length=avg_sentence_length,
            avg_word_length=avg_word_length,
            formal_score=formal_score,
            informal_score=informal_score
        ) 