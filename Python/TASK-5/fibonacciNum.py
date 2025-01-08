"""
    sum of non fib number for given number of range
"""
num = int(input("Enter a number: "))
a,b,count,nonFibNum=0,1,0,0
while count!=num:
    for i in range(a+1,b):
        count+=1
        nonFibNum+=i
        if count==num:
            break
    a,b=b,a+b
print(nonFibNum)

'''
input: Enter no. of non-fib series: 3
output: 17
'''