# for max even

# num = input("Enter numbers: ")
# max1= 0
# for i in range(1,len(num)):
#     x=int(num[i])
#     if x%2 == 0 and x> max1:
#         max1=x
# print(max1)

# for even min

# using while
# num=input("Enter number: ")
# max1=num[0]
# min1=num[0]
# i=1
# while i < len(num):
#     if num[i] > max1:
#         max1=num[i]
#     if num[i] < min1:
#         min1=num[i]
#     i=i+1
# print(max1,min1)

# str1= "hello"
# print(str1.capitalize()) # Hello

# str2="Hello world"
# print(str2.count('l')) # 3

# to find number of alpha, digits, special characters
# str1=input("Enter string: ")
# alpha=0
# num=0
# s_char=0
# for i in str1:
#     if i.isalpha():
#         alpha=alpha+1
#     elif i.isdigit():
#         num=num+1
#     else:
#         s_char=s_char+1

# print(f"alpha:{alpha}\nNumber: {num}\nSpecial char: {s_char}")

# without methods

# str1=input("Enter string: ")
# alpha=0
# num=0
# s_char=0
# for i in str1:
#     if (i>='A' and i<='Z') or (i>='a' and i<='z'):
#         alpha=alpha+1
#     elif i>='0' and i<='9':
#         num=num+1
#     else:
#         s_char=s_char+1

# print(f"alpha:{alpha}\nNumber: {num}\nSpecial char: {s_char}")

# without methods with while

# str1=input("Enter string: ")
# alpha=0
# num=0
# s_char=0
# i=0
# while i<len(str1):
#     if (str1[i]>='A' and str1[i]<='Z') or (str1[i]>='a' and str1[i]<='z'):
#         alpha=alpha+1
#     elif str1[i]>='0' and str1[i]<='9':
#         num=num+1
#     else:
#         s_char=s_char+1
#     i=i+1
# print(f"alpha:{alpha}\nNumber: {num}\nSpecial char: {s_char}")

# wap check which count is more alpha, number,special characters using while loop

# str1=input("Enter string: ")
# alpha=0
# num=0
# s_char=0
# for i in str1:
#     if i.isalpha():
#         alpha=alpha+1
#     elif i.isdigit():
#         num=num+1
#     else:
#         s_char=s_char+1

# if alpha > num and alpha>s_char:
#     print("Alphabets are more.")
# elif num > alpha and num > s_char:
#     print("Numbers are more")
# else:
#     print("Special Characters are more")

# str1=input("Enter string: ")
# alpha=0
# num=0
# s_char=0
# for i in str1:
#     if i.isalpha():
#         alpha=alpha+1
#     elif i.isdigit():
#         num=num+1
#     else:
#         s_char=s_char+1

# if alpha > num and alpha>s_char:
#     print("Alphabets are more.")
# elif num > alpha and num > s_char:
#     print("Numbers are more")
# else:
#     print("Special Characters are more")


