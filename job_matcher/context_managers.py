import time
import logging
from contextlib import contextmanager
from collections.abc import Iterator


logger = logging.getLogger(__name__)

@contextmanager
def measure_block(name: str) -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        duration_ms = (time.perf_counter() - start) * 1000        
        logger.debug(f"{name} executed in {duration_ms:.3f} ms")
