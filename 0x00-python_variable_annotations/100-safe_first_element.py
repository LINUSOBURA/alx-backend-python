#!/usr/bin/env python3
"""100-safe_first_element.py"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the given list if it is not empty,
    otherwise returns None.

    Parameters:
        lst (Sequence[Any]): The list from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the list if it is not empty,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
