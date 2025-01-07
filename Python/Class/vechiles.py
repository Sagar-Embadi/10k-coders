'''
    INPUT:
    200 - value of v(vehicles)
    540 - value of w(wheels)

    OUTPUT:
    TW: 130 FW: 70

    EXPLANATION:
    130 + 70 = 200 (vehicles)
    (130*2) + (70*4) = 540 (wheels)
'''

v=int(input("Enter no of Vehicles: "))
w=int(input("Enter no.of Wheels: "))

x=(4*v -w)//2

print(f"TW = {x} FW = {v-x}")

'''
    x+y = v => y = v-x
    2x + 4y = w
    2x + 4(v-x) = w
    4v - 2x = w
    x = (4v-w)/2
'''