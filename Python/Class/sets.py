'''
    SETs in Python
    def: set is a collection of elements of diff dataTypes, which are separated by commas and enclosed within flower brackets {}
    * set doesn't allow duplicates
    * Indexing is not possible
    * set is unordered 
'''

# s1={2,5,7,2,True,"A","A","a"}
# print(s1)

# l=[2,3,4,5,2,3]
# s=set(l)
# print(s)
# print(list(s),tuple(s))

'''
    Set methods
'''

# s1={1,3,5,7,9}
# s2={0,2,4,6,8}
# s2.add(10) # adding single element to set
# print(s2)
# s1.update(s2) # adding set to another set
# print(s1)

# s1={1,3,5,7,9}
# s1.clear() # removes al the elements in the set
# print(s1)

# s1={1,3,5,7,9}
# s1.remove(9) # remove the particular element, through error when we remove the element which is not there in the set
# print(s1)

# s1={1,3,5,7,9}
# s1.discard(20) # remove the particular element, it doesn't through error when we remove the element which is not there in the set
# print(s1)

# s1={1,3,5,7,9}
# s1.pop() # removes last element in list, But in set it removes random element BCuz set is unordered.
# print(s1)

A={1,2,3,4}
B={3,4,5,6}
# print(A.union(B)) 
# print(A | B)
# print(A.intersection(B))
# print(A & B)
# print(A.difference(B))
# print(A - B)