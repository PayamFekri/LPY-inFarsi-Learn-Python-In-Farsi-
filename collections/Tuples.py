#Tuples : can not change (not add , not remove)
my_tuple = ('apple' , 'graps' , 'mango' , 'graps')
print(my_tuple[2])


# list & tuple : (zip)
print(list(zip([1,3,2],[5,9,7])))

# unzip:
z = [(1, 5), (3, 9), (2, 7)]
unzip = lambda z :list(zip(*z))
print(unzip(z))

# Concatination:
my_tuple = my_tuple + ('a',)
print(my_tuple)

# Repitition :
print(my_tuple*2)

# Check Membership :
print(1 in (2,1,4,3))

# Iterating over Tuples:
for i in range(len(('A',1,'B',2))): #A*1*B*2*
    print(('A',1,'B',2)[i],end='*')
    
