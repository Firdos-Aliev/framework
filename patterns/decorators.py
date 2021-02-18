import time


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function time: {time.time() - start}")
        return result

    return wrapper


#def app(path):
#    def wrapper(func):
#        print(path)
#        print(func)
#        # urls[path] = func
#
#    return wrapper
