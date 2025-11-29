import time
from functools import wraps
from src.core.logger import get_logger

logger = get_logger(__name__)

def profile_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            logger.debug(f"{func.__name__} took {execution_time:.3f}s")
            
            return result
        
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"{func.__name__} failed after {execution_time:.3f}s: {e}")
            raise
    
    return wrapper
