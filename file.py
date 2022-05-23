from functools import wraps

def greeter(func):
    @wraps(func)
    def inner(*args):
        name = func(*args).title()
        result = f'Aloha {name}'
        return result
    return inner


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
