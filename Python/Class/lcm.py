'''
    LCM of 2 numbers
'''
# a=int(input("Enter number-1: "))
# b=int(input("Enter number-2: "))
# max1=a if (a>b) else b
# temp=max1
# while True:
#     if temp%a==0 and temp%b==0:
#         print("LCM is:",temp)
#         break
#     temp+=max1
    
# print("GCD:",(a*b)//temp) # GCD using LCM

'''
    GCD of 2 numbers
'''
# a=int(input("Enter number-1: "))
# b=int(input("Enter number-2: "))

# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print("GCD:",gcd)

# print("LCM:",(a*b)//gcd) # LCM using GCD

'''
    LCM without methods
'''
# def LCM(a,b):
#     max1=a if (a>b) else b
#     temp=max1
#     while True:
#         if temp%a==0 and temp%b==0:
#             # print("LCM is:",temp)
#             break
#         temp+=max1
#     return temp
# # import math
# digits=[int(i) for i in input("Enter number: ")]
# lcm=digits[0]
# for i in range(1,len(digits)):
#     lcm+=LCM(lcm,digits[i])
# print("LCM:",lcm)

'''
    with math library
'''
# import math
# digits=[int(i) for i in input("Enter number: ")]
# lcm=digits[0]
# for i in range(1,len(digits)):
#     lcm = lcm*digits[i]//math.gcd(lcm,digits[i])
# print("LCM:",lcm)