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

#

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