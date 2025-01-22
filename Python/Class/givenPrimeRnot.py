num = input()
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True
    return False
prime=True
for i in num:
    if ( not isPrime(int(i))):
        prime=False
        break
print(prime)