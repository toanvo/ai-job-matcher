import time
import logging
from functools import wraps


logger = logging.getLogger(__name__)

def measure_execution_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration_ms = (time.perf_counter() - start) * 1000              
            logger.debug(f"{func.__name__} executed in {duration_ms:.3f} ms")

    return wrapper