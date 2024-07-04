#!/usr/bin/env python3
"""
101-safely_get_value.py
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on a given key.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to retrieve the value for.
        default (Union[T, None]): The default value to return if the key
        is not found in the dictionary.

    Returns:
        Union[Any, T]: The value associated with the given key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
