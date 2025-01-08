'''
    Finding prime numbers , if given number is not prime print left and right nearest prime for given number
'''
num = int(input("Enter a number: "))
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i ==0:
                return False
        return True
    return False
if (isPrime(num)):
    print("It is Prime number")
else:
    lp,rp = num-1,num+1
    while True:
        if isPrime(lp):
            lp=lp
            break
        lp -=1
    while True:
        if isPrime(rp):
            rp=rp
            break
        rp+=1
    if (rp-num) == (num-lp):
        print(lp,rp)
    elif (rp-num) < (num-lp):
        print(rp)
    else:
        print(lp)

'''
    input: Enter number: 18
    output: 17 19
    input: Enter number: 25
    output: 23
'''