from functools import wraps

def greeter(func):
    @wraps(func)
    def inner(*args):
        name = func(*args).title()
        result = f'Aloha {name}'
        return result
    return inner


def sums_of_str_elements_are_equal(func):
    def add_digits(n, i: int):
        num_str = [x for x in n[i] if x.isdigit()]
        num_int = [int(x) for x in num_str]
        my_sum = sum(num_int)
        if n[i][0] == '-':
            my_sum = -my_sum

        return my_sum

    @wraps(func)
    def get_sum(num):
        numbers = func(num).split(' ')
        sum1 = add_digits(numbers, 0)
        sum2 = add_digits(numbers, 1)

        if sum1 == sum2:
            return f"{sum1} == {sum2}"
        else:
            return f"{sum1} != {sum2}"

    return get_sum



def format_output(*required_keys):
    def outer(func):
        def inner(*args):
            input = func(*args)
            result = {}
            for key in required_keys:
                if '__' in key:
                    keys = key.split('__')
                    for single_key in keys:
                        if single_key not in input:
                            raise ValueError

                    result[key] = ""
                    for i in range(len(keys)):
                        result[key] = result[key] + input[keys[i]] + " "
                    result[key] = result[key][:-1]

                else:
                    if key in input:
                        if input[key] != "":
                            result[key] = input[key]
                        else:
                            result[key] = "Empty value"
                    else:
                        raise ValueError

            return result
        return inner
    return outer


def add_method_to_instance(klass):
    def outer(func):
        def inner(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, inner)
        return inner
    return outer
