'''
         *
        * *
       * * *
      * * * *
       * * *
        * *
         *
'''
# rows = int(input("Enter rows: "))
# for i in range(1,2*rows):
#     stars = i if i<=rows else 2*rows-i
#     spaces = rows-i if i<=rows else i-rows
#     print(" "*spaces,end="")
#     print("* "*stars,end="\n")
#     # print()
'''
          1 
        2 1 2
      3 2 1 2 3
    4 3 2 1 2 3 4
'''
# rows = int(input("Enter rows: "))
# for i in range(1,rows+1):
#     res = ""
#     rev = ""
#     print(" "*(2*(rows-i)),end="")
#     for j in range(1,i+1):
#         res+=str(j)+" "
#         if j>1:
#             rev = str(j)+" "+rev
#     print(rev+res)
'''
         * 
       * *
     * * *
   * * * *
 * * * * *
'''
rows = int(input("Enter rows: "))
for i in range(1,rows+1):
    print(" "*(2*(rows-i)),end="")
    print("* "*(i))
'''
    * * * * * 
      * * * *
        * * *
          * *
            *
''' 
print()
rows = int(input("Enter rows: "))
print()
for i in range(rows,-1,-1):
    print(" "*(2*(rows-i)),end="")
    print("* "*(i))