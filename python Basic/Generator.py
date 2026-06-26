# Generator 
# yield

def count_up_to(n):
    count = 1 
    while count <= n :
        yield count
        count += 1 

counter = count_up_to(4)
print()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) # StopIteration

# Gen Expression :
my_Gen = (x*2 for x in range(10))
print(my_Gen)
print(next(my_Gen))
print(next(my_Gen))
print(next(my_Gen))
print(next(my_Gen))