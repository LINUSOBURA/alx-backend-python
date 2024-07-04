#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair into a tuple of strings.

    Args:
        k (str): The key.
        v (Union[int, float]): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key as a string
        and the value as a float.
    """
    return (k, float(v * v))
