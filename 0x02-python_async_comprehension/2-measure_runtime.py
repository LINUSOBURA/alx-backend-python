#!/usr/bin/env python3
"""
Parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function to measure the runtime of the async code block.
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop = time.time()

    return stop - start
