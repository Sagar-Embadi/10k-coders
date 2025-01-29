'''
    *
    * *
    * * *
    * * * *
'''
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    for star in range(1,i+1):
        print("*",end=" ")
    print()
'''
    1
    1 2 
    1 2 3 
    1 2 3 4
'''
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
    5 4 3 2 1 
    4 3 2 1 
    3 2 1 
    2 1 
    1 
'''
rows = int(input("Enter rows: "))
for i in range(rows,-1,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    for j in range(rows-1+i,0,-1):
        print(j,end=" ")
    print()

'''
    Number Changing Pyramid 

    1 
    2 3 
    4 5 6 
    7 8 9 10
'''
rows = int(input("Enter rows: "))
value = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(value,end=" ")
        value+=1
    print()

'''
    zeroes and ones triangle Pyramid Pattern 
    
    1 
    0 1 
    1 0 1 
    0 1 0 1
'''
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if i%2 == 1:
            if j%2 == 1:
                print(1, end=" ")
            else:
                print(0, end=" ")
        else:
            if j%2 == 1:
                print(0, end=" ")
            else:
                print(1, end=" ")
    print()
'''
    1 
    2 5 
    3 6 8
    4 7 9 10
'''
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    res = str(i)
    value = i
    for j in range(1,i):
        value+=rows-j
        res+=" "+str(value)
    print(res)