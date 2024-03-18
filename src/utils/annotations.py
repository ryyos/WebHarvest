from typing import Any, Callable, Tuple
from time import perf_counter
from functools import wraps

from src.utils import Stream
class Annotations:

    @staticmethod
    def stopwatch(func: Callable[..., Any]) -> Callable[..., Any]:
        async def inner(self, *args: Tuple, **kwargs: Any) -> Any:
            start: float = perf_counter()

            result: Any = await func(self, *args, **kwargs)

            Stream.end(start, perf_counter())
            return result

        return inner
        ...