from datetime import datetime

def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 18:
            func()
        else:
            pass
    return wrapper

@working_hours
def writting_text():
    print('I write tests')

# writting_text()

def debug(func):
    def wrapper(*args, **kwargs):
        name_convert = [repr(a) for a in args]
        age_convert = [f'{k}=!r{v}' for k,v in kwargs]
        name_plus_age = ','.join(name_convert+age_convert)
        print(f'Call the finction named "{func.__name__}({name_plus_age})"')
        result = func(args, kwargs)
        print(f'Fucntions {func.__name__!r} result is {result!r}')
        return result
    return wrapper

@debug
def age_passed(name, age=None):
    if age is None:
        return 'Введите все параметры'
    else:
        return 'Аргуметы переданы корректно'


age_passed('Boris', 'helen', 46, 56)