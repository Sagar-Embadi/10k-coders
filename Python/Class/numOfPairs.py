'''
    finding number of pairs
'''
# items=[int(i) for i in input().split()]
# qui = list(set(items))
# pairs=0
# for i in qui:
#     count = items.count(i)
#     pair=count//2
#     if pair:
#         pairs+=pair
# print(pairs)

num = input().split()
colors = set(num)
pairs = 0
for i in colors:
    pairs+=num.count(i)//2
print(pairs)