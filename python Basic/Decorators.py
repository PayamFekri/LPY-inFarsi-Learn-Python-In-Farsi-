def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator # = (say_hello = my_decorator(say_hello))
def say_hello():
    print("Hello")
say_hello()
print('-------------')
# مثال اندازه‌گیری زمان اجرا:
import time
def timer(func):
    def warpper():
        start = time.time()
        func()
        end = time.time()
        print('time: ' , end - start)
    return warpper
@timer
def top_level():
    name = 'Payam'#input('enter top level in running:')
    print(f'top : {name}')
top_level()

# @staticmethod
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
print(MathUtils.add(4,7))

# @classmethod
class Person :
    def __init__(self,name):
        self.name = name 
    @classmethod
    def create_anonymous(cls):
        return cls('Anonymous')
p = Person.create_anonymous()
print(p.name)

class User :
    def __init__(self , username , age):
        self.username = username
        self.age = age 
    @classmethod
    def from_string(cls , data):
        username , age = data.split(',')
        return cls(username, int(age))
user = User.from_string('payam,25')
print(user)
