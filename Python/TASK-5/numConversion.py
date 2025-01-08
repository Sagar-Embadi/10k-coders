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
'''
input: Enter a number: 5
output: 101
'''