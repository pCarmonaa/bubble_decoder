class PolarizationAnalysis:
    def __init__(self, polarization_level: str, polarization_score: float,
                 absolute_terms_count: int, extreme_terms_count: int):
        self.polarization_level = polarization_level
        self.polarization_score = polarization_score
        self.absolute_terms_count = absolute_terms_count
        self.extreme_terms_count = extreme_terms_count 