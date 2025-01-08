'''
    convert binary number into decimal number
'''
# STRING METHOD -1

# num= input("Enter number: ")
# num=num[::-1]
# dec=0
# for i in range(len(num)):
#     x=int(num[i])
#     dec+=(x*(2**i))
# print(dec)

# STRING METHOD -2

# num= input("Enter number: ")
# dec=0
# for i in range(len(num)-1,-1,-1):
#     x=int(num[i])
#     dec+=(x*(2**(len(num)-i-1)))
# print(dec)

# INTEGER METHOD

# num = int(input("Enter a number: "))
# temp=num
# count=dec=0
# while num!=0:
#     rem=num%10
#     # print(rem)
#     dec = dec + (2**count)*rem
#     num = num//10
#     count+=1
# print(dec)

'''
    Converting Decimal into Binary
'''
num=int(input("Enter a number: "))
bin1=""
while num>0:
    rem=num%2
    bin1= str(rem)+bin1
    num=num//2

print(bin1)