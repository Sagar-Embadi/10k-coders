'''
    Unique & Duplicate numbers
'''
# num=input().split()
# l=[]
# uni,dup = "",""
# for i in num:
#     if i not in l:
#         l.append(i)
# for i in l:
#     if(num.count(i)==1):
#         uni+=i+" "
#     else:
#         dup+=i+" "
# print(f"Duplicates: {dup}")
# print(f"Uniques: {uni}")

'''
    without methods
'''
# l=input().split()
# ct=0
# for i in l:
#     ct+=1
# c = [""]*ct
# for i in range(ct):
#     count =1
#     for j in range(i+1,ct):
#         if l[i] == l[j]:
#             c[j]= -1
#             count +=1
# if (c[i] != -1):
#     c[i]= count
# print(c)

'''
    BY USING SETS
'''

# num=input().split()
# l=list(set(num))
# uni,dup = "",""

# for i in l:
#     if(num.count(i)==1):
#         uni+=i+" "
#     else:
#         dup+=i+" "
# print(f"Duplicates: {dup}")
# print(f"Uniques: {uni}")

# is and are in output

# num=input().split()
# l=list(set(num))
# uni,dup = [],[]

# for i in l:
#     if(num.count(i)==1):
#         uni.append(i)
#     else:
#         dup.append(i)
# dup1=" ".join(dup)
# uni1=" ".join(uni)
# if len(dup)> 1:
#     print(f"Duplicates are: {dup1}")
# elif len(dup) == 0:
#     print("There are no Duplicates")
# else:
#     print(f"Duplicates is: {dup1}")
# if len(uni)>1:
#     print(f"Uniques are: {uni1}")
# elif len(uni)==0:
#     print("There are no Uniques number")
# else:
#     print(f"Uniques is: {uni1}")

'''
    Using Dictionary
'''

# num=input("Enter numbers: ").split()
# d=dict()
# for i in num:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for i in d:
#     if d[i] == 1:
#         print(i,"uni")
#     else:
#         print(i, "dup")

'''
    Enter numbers: 1 2 3 1 2 4 5
    {'1': 2, '2': 2, '3': 1, '4': 1, '5': 1}
    1 dup
    2 dup
    3 uni
    4 uni
    5 uni
'''
# num=[int(i) for i in input("Enter numbers: ").split()]
# d={}
# for i in num:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     print(f"{i} - {d[i]}")

'''
    Enter numbers: 1 2 3 1 2 4 5
    1 - 2
    2 - 2
    3 - 1
    4 - 1
    5 - 1
'''

# num=[int(i) for i in input("Enter numbers: ").split()]
# d={}
# l=[]
# for i in num:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for i in d:
#     l.append(d[i])
