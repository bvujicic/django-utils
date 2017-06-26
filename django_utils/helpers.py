"""
Various helper functions.
"""

from django.utils.text import slugify


def null_slugify(*, value):
    """
    Wrapper around slugify that returns None for slugified values that evaluate as False.
    This is useful since slug fields at the database level are NULL for the uniqueness to work properly.

    :param value: value to slugify
    :return: slugified value or None
    """
    new_value = slugify(value)

    return new_value if new_value else None