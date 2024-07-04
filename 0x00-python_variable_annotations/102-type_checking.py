#!/usr/bin/env python3
"""
102-type_checking.py"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Generate a zoomed-in version of the given array by repeating
    each element a specified number of times.

    Parameters:
        lst (Tuple): The input array to be zoomed in.
        factor (int, optional): The number of times each element
        should be repeated. Defaults to 2.

    Returns:
        List: The zoomed-in version of the input array.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
