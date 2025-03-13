l1 = [1,2,5,4,2,-1]
res =[]
for i in range(len(l1)):
    c=0
    for j in range(i+1,len(l1)):
        if l1[j]> l1[i]:
            c+=1
            res.append(c)
            break
        else:
            c+=1
    if i==len(l1):
        res.append(-1)
res.append(-1)
    
print(res)