roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
rom = input("Enter a roman: ")
res,i=0,0
while i<len(rom):
    if i==len(rom)-1:
        res = res+roman[rom[i]]
        i+=1
    elif(roman[rom[i]]>=roman[rom[i+1]]):
        res+=roman[rom[i]]
        i+=1
    else:
        res+=(roman[rom[i+1]] - roman[rom[i]])
        i+=2
        
print(res)
        

