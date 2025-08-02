from domain.ports.driving.atomic_analyzers import PolarizationAnalyzer
from domain.models.polarization_analysis import PolarizationAnalysis

class PolarizationAnalyzerService(PolarizationAnalyzer):
    def analyze(self, content: str) -> PolarizationAnalysis:
        content_lower = content.lower()
        
        polarizing_indicators = [
            'always', 'never', 'everyone', 'nobody', 'absolutely', 'completely',
            'totally', 'extremely', 'radical', 'extreme', 'fanatic', 'zealot',
            'us vs them', 'good vs evil', 'right vs wrong'
        ]
        
        absolute_terms = ['always', 'never', 'everyone', 'nobody', 'absolutely', 'completely']
        extreme_terms = ['extremely', 'radical', 'extreme', 'fanatic', 'zealot']
        
        absolute_score = sum(content_lower.count(term) for term in absolute_terms)
        extreme_score = sum(content_lower.count(term) for term in extreme_terms)
        
        total_polarization_score = absolute_score + extreme_score
        polarization_level = min(1.0, total_polarization_score / len(content.split()) * 10)
        
        if polarization_level > 0.3:
            level = 'high'
        elif polarization_level > 0.1:
            level = 'medium'
        else:
            level = 'low'
        
        return PolarizationAnalysis(
            polarization_level=level,
            polarization_score=polarization_level,
            absolute_terms_count=absolute_score,
            extreme_terms_count=extreme_score
        ) 