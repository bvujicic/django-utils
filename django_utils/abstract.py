"""
Common abstract Django models.
"""

from django.contrib.contenttypes.fields import ContentType, GenericForeignKey
from django.db import models


class TimestampModel(models.Model):
    """
    Inheritance model for created and modified timestamp fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderModel(models.Model):
    """
    Inheritance model for odering field.
    """
    order = models.IntegerField(default=1)

    class Meta:
        abstract = True


class GenericForeignKeyModel(models.Model):
    """
    Inheritance generic foreign key model.
    Inherit from this if you want your model to have a generic foreign key to any ContentType instance.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        abstract = True