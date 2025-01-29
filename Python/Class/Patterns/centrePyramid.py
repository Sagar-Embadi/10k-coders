'''
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
'''
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    for s in range(rows-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

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

#    OR

rows = int(input("Enter rows: "))
for i in range(rows,-1,-1):
    for s in range(rows-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()