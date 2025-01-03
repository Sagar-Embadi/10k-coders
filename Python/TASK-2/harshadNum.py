num=input()
sum1=0
for i in num:
    sum1+=int(i)
if int(num) % int(sum1) == 0:
    print("Yes it is a Harshad number.")
else:
    print("No it is not a Harshad number.")