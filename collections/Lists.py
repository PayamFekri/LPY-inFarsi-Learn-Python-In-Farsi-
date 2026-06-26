# name-list = []
# move in list : name-list[start-index : end-index : step]
# lists are full RAM and get big RAM! Disadvantages
mylist= [3,56,12,37,91,'pay' , True , 'ejuhfejk' , 74]
print(mylist[1:6:1])

#add to list: name-list.insert(  index,<Content> )
mylist.insert(4 ,'li')

# list Expressions : 
# # new_list[<action> for <item> in <iterator> if <some condition>]
print([i for i in range(10,40) if i%3 ==0])
print([sum(pair) for pair in zip([4,2,8],[10,7,3])])

# Get First and Last element of a list
first, *x, last = mylist
print(first , last)

print(list('PayamFekri'))
sorted_by_key = sorted([
                       {'name': 'Bina', 'age': 30},
                       {'name':'Andy', 'age': 18},
                       {'name': 'Zoey', 'age': 55}],
                       key=lambda el: (el['name']))
print(sorted_by_key)


# Read line of a file into a list:

#with open("myfile.txt") as f:
#  lines = [line.strip() for line in f]