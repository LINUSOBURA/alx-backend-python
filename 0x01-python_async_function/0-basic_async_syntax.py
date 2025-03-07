#!/usr/bin/env python3
"""
Basic async syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0
    and `max_delay` seconds.

    Args:
        max_delay (int, optional): The maximum delay in
        seconds. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
