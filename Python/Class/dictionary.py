'''
        DICTIONARY in Python
        def: It is a collection of items in the form of key: value pair, Which are separated by comma and enclosed with flower brackets{}

        PROPERTIES:
        * Ordered
        * Indexing is not Possible
        * Duplicate Keys are not allowed
        * Duplicate values are allowed
'''

d1=dict(name="Sagar",id=1,age=22)
# print(d1)

# print(d1.get("name"))  # get method used to get the value of key entered in get method

# print(d1.keys()) # prints all the keys in dictionary
# print(d1.values()) # prints all the values in dictionary
# print(d1.items()) # prints all the key:value pairs in the dictionary

# adding key: value

# d1["Education"]="B.Tech"
# print(d1)

# d1.pop("id")# removes a particular key value by using key in pop method
# print(d1) 

# d1.popitem() # removes last item
# print(d1)

# d1.clear() # removes all the item and returns empty dictionary
# print(d1)

# del d1  # delete the dictionary
# print(d1)

'''
    interchanging keys and values 
'''
# d1=dict(name="Sagar",id=1,age=22)
# temp={}
# print(d1)
# for i in d1:
#     temp[d1[i]] = i
# print(temp)