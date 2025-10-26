

def exact_count_args(count):
    def decorator(func):
        def inner(*args):
            args_count = len(*args)

            if args_count < count:
                return "Error: Not enough arguments"

            if args_count > count:
                return "Error: Too many arguments"

            return func(*args)
        return inner
    return decorator

def input_error(store):
    def decorator(func):
        @exact_count_args(2)
        def inner(*args):
            arguments = list(*args)
            try:
                name, phone = arguments

                if name in store:
                    return "Can't add. Username exists. Please, use command 'change' to set new phone."

                return func(arguments)
            except ValueError:
                return "Give me name and phone please."

        return inner
    return decorator

def change_contact_error(store):
    def decorator(func):
        @exact_count_args(2)
        def inner(*args):
            arguments = list(*args)
            try:
                name, phone = arguments

                if name not in store:
                    return f"Can't change. Contact '{name}' doesn't exists."

                return func(arguments)
            except ValueError:
                return "Give me name and phone please."

        return inner
    return decorator
