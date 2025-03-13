'''
1       5 
  2   4   
    3     
  2   4   
1       5 
'''
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==j or j==rows-i+1:
            print(j,end=" ")
        else:
            print("  ",end="")
    print()

'''
        1
       *2*
      **3**
     ***4***
    ****5****
'''
r = int(input("R: "))
for i in range(1,r+1):
    st = "*"*(i-1)
    sp = " "*(r-i)
    print(f"{sp}{st}{i}{st}")