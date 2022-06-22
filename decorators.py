import datetime

def log_decorator(old_function):
    def new_function(*args, **kwargs):
        dt = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        text = f"Function {old_function.__name__} was called with parameters: "
        with open('function_log.log', 'a') as doc:
            doc.write(str(dt))
            doc.write('\n')
            doc.write(text)
            doc.write(*args, **kwargs)
            doc.write('\n')
            doc.write(str(result))
            doc.write('\n')
            doc.write('\n')
        return result

    return new_function


def log_param_decorator(path: str):
    def log_decorator_f(old_function):
        def new_function(*args, **kwargs):
            dt = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            text = f"Function {old_function.__name__} was called with parameters: "
            with open(path, 'a') as doc:
                doc.write(str(dt))
                doc.write('\n')
                doc.write(text)
                doc.write(*args, **kwargs)
                doc.write('\n')
                doc.write(str(result))
                doc.write('\n')
                doc.write('\n')
            return result

        return new_function

    return log_decorator_f