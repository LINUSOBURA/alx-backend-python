#!/usr/bin/env python3
"""
measure Runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken to run the `wait_n` function
    asynchronously `n` times with a maximum delay of `max_delay`.

    Args:
        n (int): The number of times to run the `wait_n` function.
        max_delay (int): The maximum delay for each asynchronous call.

    Returns:
        float: The average time taken for each asynchronous call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    return elapsed_time / n
