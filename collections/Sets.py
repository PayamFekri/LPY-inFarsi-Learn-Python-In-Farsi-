# Set : there is not duplicate members.

# create set : 
s = set()
# add to set 
s.add(3435)
s.add('pasdswkmf')
print(s)
s.update([4,33,56,75,234,76,18])
print(s)

s.update('ef')
print(s)

s.add('gh')
print(s)

print(set('ab'))

# remove elements from set : 
s.remove(4)#  Raises KeyError if element not found
s.discard(4) # Doesn't raise an error if element not found
print(s)

# Set operation 
s1 = {1,2,3}
s2 = {2,3,4,6,7,0}
# Union : 
print( {1,2,3}|{2,3,4,6,7,0})
print( s1.union(s2))

# Intersection
print( {1,2,3}&{2,3,4,6,7,0})
print( s1.intersection(s2))

# Difference
print( {1,2,3}-{2,3,4,6,7,0})
print( s1.difference(s2))

# Symmetric Difference
print( {1,2,3}^{2,3,4,6,7,0})
print( s1.symmetric_difference(s2))

# Subset
print( {1,2,3}>{2,3,4,6,7,0})
print( s1.issubset(s2))

# Superset
print( {1,2,3}<{2,3,4,6,7,0})
print( s1.issuperset(s2))

# Iterating over Sets
for e in{0,'a',1}:
    print(e,end='>')