#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Calculates the sum of a list of mixed floats and integers.

    Args:
        mxd_lst (List[Union[float, int]]): A list of floats and integers.

    Returns:
        float: The sum of all the floats and integers in the list.
    """
    return sum(mxd_lst)
