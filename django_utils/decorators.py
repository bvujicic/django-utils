"""
Various useful decorators.
"""

from django.core.exceptions import FieldDoesNotExist


def modify_field_attributes(**kwargs):
    """
    Class decorator on models.Model class.

    When common fields are inherited through abstract models, their attributes can't be changed at construction time.
    Decorate the class with a mapping of keys that correspond to field names and values that correspond to mapping of
    attributes that need overriding.

    Example:
        @modify_field_attributes(
            {'name': {'verbose_name': 'alternative_name'}, 'content': {'unique': True}}
        )
        class ConcereteModel(NameBastractModel, ContentAbstractModel):
            pass

    """
    def wrapper(cls):

        for key, value in kwargs.items():

            # if parameter is not a field name, just set a class attribute
            try:
                field = cls._meta.get_field(key)

            except FieldDoesNotExist:
                setattr(cls, key, value)
                continue

            else:
                # traverse the dict containing properties and values for a field
                for field_attribute, field_attribute_value in value.items():
                    setattr(field, field_attribute, field_attribute_value)

        return cls

    return wrapper
