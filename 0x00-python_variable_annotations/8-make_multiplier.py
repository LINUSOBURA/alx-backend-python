#!/usr/bin/env python3
"""8-make_multiplier.py"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the
    provided multiplier.

    Parameters:
        multiplier (float): The number by which the input
        float will be multiplied.

    Returns:
        Callable[[float], float]: A function that multiplies
        a given float by the provided multiplier.
    """
    return lambda x: x * multiplier
