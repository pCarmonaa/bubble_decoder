import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Dict
from domain.ports.driven.external_emotional_analyzer import ExternalEmotionalAnalyzer
from domain.models.emotion.emotion_data import EmotionData


class LlmEmotionalAnalyzerAdapter(ExternalEmotionalAnalyzer):
    def __init__(self):
        emotion_model_name = "SamLowe/roberta-base-go_emotions"
        self.emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
        self.emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
        
        self.emotion_labels = [emotion for emotions in EmotionData.CATEGORIES.values() for emotion in emotions]

    def get_emotional_analysis(self, text: str) -> Dict[str, float]:
        emotion_inputs = self.emotion_tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            emotion_outputs = self.emotion_model(**emotion_inputs)
            emotion_scores = torch.nn.functional.softmax(emotion_outputs.logits, dim=1)
            
        return {
            self.emotion_labels[i]: float(emotion_scores[0][i])
            for i in range(len(self.emotion_labels))
        }