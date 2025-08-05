from abc import abstractmethod
from typing import Dict


class ExternalEmotionalAnalyzer:
    @abstractmethod
    def get_emotional_analysis(self, text: str) -> Dict[str, float]:
        pass
