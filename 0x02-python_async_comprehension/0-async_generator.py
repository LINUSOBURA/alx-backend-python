#!/usr/bin/env python3
"""
Async_generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Asynchronous generator that yields random floats between 0
    and 10 after a 1-second delay, repeated 10 times.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
