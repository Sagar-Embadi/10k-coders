'''
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
'''
rows = int(input("Enter rows: "))
for i in range(rows,-1,-1):
    print(" "*(rows-i)+"* "*i)
'''
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
'''
rows = int(input("Enter rows: "))
print()
for i in range(1, rows+1):
    for s in range(rows-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

'''
    1 2 3 4 5
    1 2 3 4 
    1 2 3 
    1 2
    1
'''
rows = int(input("Enter rows: "))
print()
for i in range(rows,-1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

