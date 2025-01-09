'''
    checking given number is armstrong or not
'''
# num = input("Enter a number: ")
# power=len(num)
# res=0
# for i in num:
#     res+= int(i)**power
# print(res==int(num))

'''
    Finding armstrong numbers btw given range
'''
num1 = int(input("Enter a number: "))
def armstrong(num):
    res,power = 0,len(num)
    for i in num:
        res+= int(i)**power
    return num==str(res)
for i in range(1,num1+1):
    if(armstrong(str(i))):
        print(i)