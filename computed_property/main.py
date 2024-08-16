import functools


def computed_property(*args):
    """
    Decorator to create a computed property that caches its result based on specified attributes.

    Args:
        :param args: Attribute names that the computed property depends on.

    Returns:
        :return function: The decorated function with caching behavior.
    """
    def decorator(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(self):
            current = tuple(getattr(self, arg) for arg in args if isinstance(arg, str))
            if current != cache.get("values"):
                cache["values"] = current
                cache["result"] = func(self)
            return cache["result"]

        def setter(self, value):
            cache.clear()
            func(self, value)

        def deleter(self):
            cache.clear()
            func(self)

        wrapper.setter = setter
        wrapper.deleter = deleter
        return wrapper

    return decorator
