'''
    checking perfect number or not
'''
# num= int(input("Enter a number: "))
# sum1=0
# for i in range(1,(num//2)+1):
#     if num%i==0:
#         sum1+=i
# print(sum1==num)
'''
    finding perfect numbers in the range of given number
'''
num= int(input("Enter a number: "))
def perfect(num):
    sum1=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum1+=i
    return (sum1==num)
for i in range(1,num+1):
    if(perfect(i)):
        print(i)