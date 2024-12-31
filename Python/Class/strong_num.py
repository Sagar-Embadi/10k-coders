# num=input("Enter digits: ")
# sum1=0
# for i in num:
#     x=int(i)
#     fact=1
#     for j in range(1,x+1):
#         fact*=j
#     sum1+=fact
# if sum1==int(num):
#     print("strong Number")
# else:
#     print("not a Strong Number")

# program to find strong numbers in btw userInput number
# num=int(input("Enter a number: "))
# for i in range(1,num+1):
#     iStr=str(i)
#     res=0
#     for j in iStr:
#         fact=1
#         for k in range(1,int(j)+1):
#             fact*=k
#         res+=fact
#     if res == i:
#         print(i)