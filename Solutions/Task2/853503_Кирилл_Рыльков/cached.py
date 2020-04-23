def cached(function):
    memory = {}

    def wrapper(*args, **kwargs):
        if args in memory:
            return memory[args]
        else:
            memory[args] = function(*args, **kwargs)
            return memory[args]
    return wrapper
