#!/usr/bin/env python3
"""8-make_multiplier.py"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input iterable and its length.
    
    :param lst: An iterable of sequences (e.g., lists, tuples, strings).
    :type lst: Iterable[Sequence]
    :return: A list of tuples where each tuple contains an element from the input iterable and its length.
    :rtype: List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
