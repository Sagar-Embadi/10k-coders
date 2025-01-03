num=input()
emp=""
for i in num:
    if i == '0':
        emp+="1"
    elif i== '1':
        emp+='0'
    else:
        emp+=i
        
print(emp)