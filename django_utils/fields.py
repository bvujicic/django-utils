"""
Django model fields.
"""

from django.db.models import SlugField as BaseSlugField


class SlugField(BaseSlugField):
    """
    Adds an attribute to slug field that holds a field name to populate from.
    """
    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop('populate_from', None)

        super().__init__(*args, **kwargs)
