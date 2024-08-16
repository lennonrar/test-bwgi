import functools

def computed_property(*args):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(self):
            current = tuple(getattr(self, arg) for arg in args if isinstance(arg, str))
            if current != cache.get('values'):
                cache['values'] = current
                cache['result'] = func(self)
            return cache['result']

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
