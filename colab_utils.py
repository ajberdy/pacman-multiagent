from functools import wraps


def use_function(class_name):
    def decorated_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            setattr(globals()[class_name], decorated_function.__name__, wrapper)
            function(*args, **kwargs)

        return wrapper
    return decorated_function
