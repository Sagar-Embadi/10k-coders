'''
    checking given digits is fib or not, if fib sum those numbers
    input: 52409
    output: 7
'''
# num = input("Enter numbers: ")
# fibSum=0
# def is_fib(n):
#     a,b=0,1
#     while True:
#         if a == n:
#             return True
#         if a>n :
#             return False
#         a,b=b,a+b
# for i in num:
#     if(is_fib(int(i))):
#         fibSum+=int(i)
# print(fibSum)
'''
    finding nearest fib number to given number 
'''

num = int(input("Enter numbers: "))
def is_fib(n):
    a,b=0,1
    while True:
        if a>n :
            return  a,(b-a)
        a,b=b,a+b
# print(is_fib(num))
# print(is_fib(num)[0]-num)
# print(is_fib(num)[1]-num)
if(is_fib(num)[0]-num) > (num-is_fib(num)[1]):
    print(is_fib(num)[1])
else:
    print(is_fib(num)[0])
    
'''
    finding nearest fib number to given number or if it present in series print that number
'''
# num = int(input("Enter numbers: "))
# def is_fib(n):
#     a,b=0,1
#     while True:
#         if a==n:
#             return(a)
#         if a>n :
#             return  a,b-a
#         a,b=b,a+b
# # print(is_fib(num))
# if(is_fib(num)==num):
#     print(num)
# elif(is_fib(num)[0]-num) > (is_fib(num)[1]-num):
#     print(is_fib(num)[1])
# else:
#     print(is_fib(num)[0])