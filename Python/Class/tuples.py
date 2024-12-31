'''
    ### TUPLES in Python
    def: tuple is a collection of elements of diff dataTypes, which are separated by commas and enclosed within parenthesis ()
    
    
    * it is immutable (can't add , delete elements)
    * can access through index values
    * t1 = (1,2,3,5,True,"sagar")
'''

# ""t1=tuple((2,3,4,"A"))
# print(t1,type(t1))

# t2=(2,4,6,True)
# print(t2)

# t3=("hello",) # use comma to convert it into tuple otherwise it will be treated as string
# print(t3, type(t3))

# t4= 2,3,1,"s"
# print(t4, type(t4))""

# to add, delete , updating elements in tuple 
# convert it in to list and after modification again convert it into tuple

# t1 = tuple((2,3,4))
# l1=list(t1)
# l1.append(5)
# print(tuple(l1))

# "in" & "not in" operation works in both list and tuple

# t1= tuple(2,3,4,5)
# print(2 in t1)
# print(5 not in t1)

'''
    iterating tuples
'''

# t1= (2,5,7,9,11)
# for i in t1:
#     print(i, end=" ")
# print()
# for i in range(0, len(t1)):
#     print(t1[i], end=" ")

'''
    tuple methods
'''

# t1= (2,5,7,9,11,2,5,2,1,6,2,9,2)
# print(t1.count(2)) # 5
# print(t1.index(1)) # 8

