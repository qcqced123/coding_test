import sys
from time import perf_counter
from functools import lru_cache
from typing import List


try:
    profile
except NameError:
    profile = lambda x: x


@lru_cache
@profile
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    start = perf_counter()
    result = fibonacci(50)
    end = perf_counter()

    print(f"{result}")
    print(f"{end - start} seconds are consumed")