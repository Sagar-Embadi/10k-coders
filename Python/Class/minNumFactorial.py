'''
    find min num factorial in given number
'''
num=input()
min1=num[0]
for i in num:
    if min1> i:
        min1=i
res,fact="",1
for i in range(1,int(min1)+1):
    if i == int(min1):
        res+=str(i)+" ="
    else:
        res+=str(i)+"*"
    fact*=i
print(res,fact)

'''
'''

# num=[int(i) for i in input().split()]
# min1=min(num)
# res,fact="",1
# for i in range(1,int(min1)+1):
#     if i == int(min1):
#         res+=str(i)+" ="
#     else:
#         res+=str(i)+"*"
#     fact*=i
# print(res,fact)