# Closure
# nested function

def outer_function(x):
    def inner_function(y):
        return x + y   # x از تابع بیرونی گرفته می‌شود
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # 8
print(add_five(10)) # 15