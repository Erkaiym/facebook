import re

def address(path):
    def wrapper(func):
        def wrap_func(*args, **kwargs):
            request = args[0]
            match_object = re.search(r'GET\s/(\w+)', request).groups()
            print(match_object[0])
            if path == match_object[0]:
               func(*args, **kwargs)
            else:
                kwargs['match'] = False
                func(*args, **kwargs)

        return wrap_func
    return wrapper