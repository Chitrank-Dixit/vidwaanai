from typing import List, Dict
from src.core.logger import get_logger

logger = get_logger(__name__)

class FeedbackReranker:
    def __init__(self):
        self.positive_feedback = {}
        self.negative_feedback = {}
    
    def add_positive_feedback(self, query: str, doc_id: str):
        """User marked result as helpful"""
        if query not in self.positive_feedback:
            self.positive_feedback[query] = []
        if doc_id not in self.positive_feedback[query]:
            self.positive_feedback[query].append(doc_id)
            logger.info(f"Added positive feedback for query '{query}', doc {doc_id}")
    
    def add_negative_feedback(self, query: str, doc_id: str):
        """User marked result as unhelpful"""
        if query not in self.negative_feedback:
            self.negative_feedback[query] = []
        if doc_id not in self.negative_feedback[query]:
            self.negative_feedback[query].append(doc_id)
            logger.info(f"Added negative feedback for query '{query}', doc {doc_id}")
    
    def get_feedback_score(self, query: str, doc_id: str) -> float:
        """Get feedback score for document"""
        positive_list = self.positive_feedback.get(query, [])
        negative_list = self.negative_feedback.get(query, [])
        
        positive_count = len(positive_list)
        negative_count = len(negative_list)
        
        doc_positive = (1 if doc_id in positive_list else 0)
        # doc_negative = (1 if doc_id in negative_list else 0) # Not used in formula but good to know
        
        if positive_count + negative_count == 0:
            return 0.5  # Neutral if no feedback
        
        # Simple Bayesian average-like score
        return (positive_count + doc_positive) / (positive_count + negative_count + 1)
    
    def rerank_with_feedback(self, query: str, documents: List[Dict]) -> List[Dict]:
        """Rerank considering user feedback"""
        
        for doc in documents:
            doc_id = str(doc.get('id', ''))
            feedback_score = self.get_feedback_score(query, doc_id)
            doc['feedback_score'] = feedback_score
            
            # Combine original score (normalized) with feedback score
            # Assuming 'score' is already normalized or roughly 0-1. If not, this might skew.
            original_score = doc.get('score', 0.5)
            # Normalize if > 1 (e.g. BM25 scores)
            if original_score > 1.0: 
                original_score = 1.0 # Cap for simple combination
                
            doc['final_score'] = (original_score * 0.7) + (feedback_score * 0.3)
        
        return sorted(documents, key=lambda x: x['final_score'], reverse=True)
