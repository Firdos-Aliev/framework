import time


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function time: {time.time() - start}")
        return result

    return wrapper

