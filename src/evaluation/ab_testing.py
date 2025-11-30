import random
from typing import Callable, Dict, List, Any
from src.core.logger import get_logger

logger = get_logger(__name__)

class ABTesting:
    def __init__(self):
        self.variant_a_results = []
        self.variant_b_results = []
    
    def run_test(self, queries: List[str], variant_a: Callable, 
                 variant_b: Callable, num_samples: int = None) -> Dict:
        """Run A/B test on variants"""
        
        if num_samples is None:
            num_samples = len(queries)
        
        test_queries = random.sample(queries, min(num_samples, len(queries)))
        logger.info(f"Starting A/B test with {len(test_queries)} queries")
        
        for query in test_queries:
            result_a = self.evaluate_variant(query, variant_a)
            result_b = self.evaluate_variant(query, variant_b)
            
            self.variant_a_results.append(result_a)
            self.variant_b_results.append(result_b)
        
        return self.generate_report()
    
    def evaluate_variant(self, query: str, variant_func: Callable) -> Dict:
        """Evaluate single query with variant"""
        import time
        start_time = time.time()
        try:
            # Variant function should return a dict with metrics or results
            # We assume it returns something we can evaluate or just the results
            result = variant_func(query)
            duration = time.time() - start_time
            
            # If result is a list (retrieved docs), we can't calculate MRR/NDCG without ground truth
            # So here we just record success and time unless the variant func returns metrics
            
            metrics = {
                'query': query,
                'success': True,
                'time': duration,
            }
            
            if isinstance(result, dict):
                metrics.update(result)
            
            return metrics
            
        except Exception as e:
            logger.error(f"Variant evaluation failed for query '{query}': {e}")
            return {
                'query': query,
                'success': False,
                'error': str(e),
                'time': time.time() - start_time
            }
    
    def generate_report(self) -> Dict:
        """Generate A/B test report"""
        report = {
            'variant_a': {
                'avg_time': self.calculate_avg('time', self.variant_a_results),
                'success_rate': self.calculate_success_rate(self.variant_a_results)
            },
            'variant_b': {
                'avg_time': self.calculate_avg('time', self.variant_b_results),
                'success_rate': self.calculate_success_rate(self.variant_b_results)
            },
            'winner': 'undetermined' # Needs specific metrics to determine
        }
        
        # If we have MRR/NDCG, add them
        if any('mrr' in r for r in self.variant_a_results):
            report['variant_a']['avg_mrr'] = self.calculate_avg('mrr', self.variant_a_results)
            report['variant_b']['avg_mrr'] = self.calculate_avg('mrr', self.variant_b_results)
            
            if report['variant_a']['avg_mrr'] > report['variant_b']['avg_mrr']:
                report['winner'] = 'variant_a'
            elif report['variant_b']['avg_mrr'] > report['variant_a']['avg_mrr']:
                report['winner'] = 'variant_b'
            else:
                report['winner'] = 'tie'
                
        return report
    
    def calculate_avg(self, metric: str, results: List[Dict]) -> float:
        """Calculate average metric"""
        valid = [r[metric] for r in results if r.get('success') and metric in r]
        return sum(valid) / len(valid) if valid else 0.0
    
    def calculate_success_rate(self, results: List[Dict]) -> float:
        """Calculate success rate"""
        if not results:
            return 0.0
        return sum(1 for r in results if r.get('success')) / len(results)
