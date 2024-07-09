#!/usr/bin/env python3
"""
Async Comprehensions
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Asynchronously comprehends the values yielded by the `async_generator`
    and returns a list of the resulting values.

    Returns:
        list: A list of the values yielded by the `async_generator`.
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
