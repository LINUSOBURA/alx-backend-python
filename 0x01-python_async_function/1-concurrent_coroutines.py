#!/usr/bin/env python3
"""
concurent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a list of n random delays, each with a
    maximum delay of max_delay.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay for each random delay.

    Returns:
        List[float]: A list of floats representing the random
        delays waited for.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task

        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
