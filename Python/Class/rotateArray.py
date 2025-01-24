'''
    shifting last index number to first index place for k times of user input 
'''
num = input().split()
k = int(input())
for i in range(k):
    x = num[-1]
    for j in range(len(num)-2,-1,-1):
        num[j+1]=num[j]
    num[0]=x
print(" ".join(num))

# num = input().split()
# k = int(input())
# def rev(x,y):
#     while x < y:
#         num[x], num[y] = num[y],num[x]
#         x,y = x+1,y-1