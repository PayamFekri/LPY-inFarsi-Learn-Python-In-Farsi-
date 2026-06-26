# Dictionary:
# structure ->name-dictionary= {key1 : value1 , key2 : value2 , ... }
# 
my_dict = {'name': 'payam' , 'age' : 29 , 'present':True}
print(my_dict['name'])

print(my_dict.keys())
print(my_dict.values())

# 1 solution : add to dict
my_dict['evidence'] = 'master'
print(my_dict)

# 2 solution : add to dict
my_dict.update({'cool':True})
{**my_dict , **{'new-col':False}}

# split column
print({
    key : value for key,value in my_dict.items() if key=='evidence' or key =='name'
})
