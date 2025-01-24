'''
    
'''
num = input().split()
for i in num:
    iStr="".join(sorted(i))
    if (iStr!=1):
        print(False)
        break
    else:
        print(True)