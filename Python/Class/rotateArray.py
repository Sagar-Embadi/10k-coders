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