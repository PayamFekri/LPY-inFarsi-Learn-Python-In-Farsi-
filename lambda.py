# lambda: <return_value>
# lambda <argument1>, <argument2>: <return_value>

from functools import reduce

n = 3 
factorial = reduce(lambda x ,y : x*y , range(1,n+1))
print(f'factorial : {factorial}')

fib = lambda n : n if n <=1 else fib(n-1) + fib(n-2)
print(f'fibonacci: {fib(5)}')

a = lambda x : x+1 , range(10)
b = map(lambda x : x+1 , range(10))
c = list(map(lambda x : x+1 , range(10)))
print('\n',a)
print(b)
print(c , '\n')


#Map,Filter
d = list(map(lambda x: x > 5, range(10))) 
print(d)
e = list(filter(lambda x: x > 5, range(10))) 
print(e)


print(all([True,1,3,True])) 
print(any([False, True, False]))
