from functools import wraps
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

def time_limit(timeout_sec: Optional[float]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(1) as executor:
                future = executor.submit(func, *args, **kwargs)
                failed = False
                try:
                    return future.result(timeout=timeout_sec)
                except concurrent.futures.TimeoutError:
                    failed = True
                if failed:
                    raise TimeoutError(
                        f"function `{func.__name__}` time limit exceeded ({timeout_sec}s)"
                    )
        return wrapper
    return decorator
