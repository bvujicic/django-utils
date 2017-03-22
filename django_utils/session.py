"""
Utilities for session processing.
"""


class SessionData:
    """
    Session object descriptor used as a class attribute on View subclasses.

    Initialize with session key.
    Retrieval retrieves value under session key.
    Assignment updates the value already existing under the key or creates a new value.

    Example:
        class ConcreteView(View):
            data = SessionData('key_name')
    """
    def __init__(self, session_key):
        self.session_key = session_key

    def __get__(self, instance, owner):
        try:
            data = instance.request.session.get(self.session_key, {})

        except AttributeError:
            raise AttributeError('Must be a class attribute on a View subclass.')

        else:
            return data

    def __set__(self, instance, value):
        try:
            instance.request.session.setdefault(self.session_key, {}).update(value)

        except AttributeError:
            raise AttributeError('Must be a class attribute on a View subclass.')

        except TypeError:
            raise TypeError('Session assignment value must be a dictionary.')

        else:
            instance.request.session.modified = True

    def __repr__(self):
        return '{cls}({init})'.format(cls=self.__class__.__name__, init=self.session_key)
