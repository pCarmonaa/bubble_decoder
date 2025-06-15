from typing import Dict, Any
from textblob import TextBlob
from domain.ports.driving.atomic_analyzers import TopicAnalyzer

class TopicAnalyzerService(TopicAnalyzer):
    def analyze(self, content: str) -> Dict[str, Any]:
        blob = TextBlob(content.lower())
        words = blob.words
        
        topic_keywords = {
            'politics': ['politics', 'government', 'election', 'vote', 'democrat', 'republican', 'policy'],
            'technology': ['technology', 'tech', 'software', 'programming', 'ai', 'machine learning', 'data'],
            'health': ['health', 'medical', 'doctor', 'hospital', 'medicine', 'treatment', 'disease'],
            'sports': ['sports', 'football', 'basketball', 'soccer', 'game', 'team', 'player'],
            'entertainment': ['movie', 'music', 'celebrity', 'film', 'actor', 'singer', 'entertainment'],
            'business': ['business', 'economy', 'market', 'company', 'finance', 'investment', 'stock'],
            'education': ['education', 'school', 'university', 'student', 'teacher', 'learning', 'study']
        }
        
        topic_scores = {}
        for topic, keywords in topic_keywords.items():
            score = sum(1 for word in words if word in keywords)
            topic_scores[topic] = score
        
        primary_topic = max(topic_scores, key=topic_scores.get) if topic_scores else 'general'
        
        return {
            'primary_topic': primary_topic,
            'topic_scores': topic_scores,
            'confidence': min(1.0, sum(topic_scores.values()) / len(words) * 10)
        } 