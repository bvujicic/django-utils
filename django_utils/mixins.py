"""
various useful Class based views' mixins.
"""

from django.conf import settings

from django_utils.helpers import null_slugify


class SlugMixin:
    """
    Model mixin for models with slug field.

    Iterate through application languages and create slugs for each language if the field it's populated from
    is not empty, once set the slug will not change.
    """
    def save(self, *args, **kwargs):
        slug_field = self._meta.get_field('slug', None)

        if getattr(slug_field, 'populate_from', None) is None:
            return super().save(*args, **kwargs)

        # populate general slug field
        self.slug = null_slugify(value=getattr(self, slug_field.populate_from))

        # populate possible translation fields, if it does not exist, ignore silently
        try:
            for lang, _ in settings.LANGUAGES:
                value = getattr(self, '{}_{}'.format(slug_field.populate_from, lang), None)

                if value is not None:
                    slug = null_slugify(value=value)
                    setattr(self, 'slug_{}'.format(lang), slug)

        except AttributeError:
            pass

        return super().save(*args, **kwargs)