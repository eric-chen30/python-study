# 装饰器：运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 函数是一个对象，可以赋值给一个变量，因此可以通过变量对函数进行调用
from datetime import datetime
import functools

# 定义一个log装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():', func.__name__)
        return func(*args, **kw)
    return wrapper

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log_text(text):
    def decorator(func):
        # 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

'''
    首先执行log_text('execute')，返回的是decorator函数
    再调用返回的函数，参数是now函数，返回值最终是wrapper函数
'''
@log_text('execute')
def now():
    print(datetime.now())

if __name__ == '__main__':
    # 将函数赋值给变量
    fn = now
    # 通过变量调用函数
    fn()
    # 函数对象有个__name__属性，可以拿到函数的名字
    # 加了@functools.wraps(func)返回的wrapper函数的__name__属性就不是wrapper了，而是func的__name__
    print(now.__name__) # 加了@functools.wraps(func)返回now，不加返回wrapper
    # print(fn.__name__)

    # 如果想增强now函数的功能，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
    # 本质上，decorator就是一个返回函数的高阶函数

