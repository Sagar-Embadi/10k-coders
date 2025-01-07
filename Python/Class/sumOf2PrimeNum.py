'''
    Given a number n,express the number as sum of 2 prime numbers
'''
num = int(input())
comb=False
def prime(n):
    if n>1:
        for j in range(2,(n//2)+1):
            if n%j == 0:
                return False
        return True
    return False
for i in range(2, num):
    if (prime(i) and prime(num-i)):
        comb=True
        break

if comb:
    print(True)
else:
    print(False)