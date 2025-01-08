num = input("Enter the digits here: ")
first=1
def is_prime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                return False
        return True
    return False
for digit in num:
    if (is_prime(int(digit))):
        if(first == 1):
            minPrime,maxPrime = int(digit),int(digit)
            first= first +1
        else:
            if int(digit) > maxPrime:
                maxPrime = int(digit)
            if int(digit) < minPrime:
                minPrime = int(digit)
print(minPrime+maxPrime)