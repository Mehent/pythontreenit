import math

class Aoc1(object):

    def __init__(self):
        pass

def calculate_fuel(mass):
    return mass//3-2

# print(calculate_fuel(100756))
sum = 0
with open('C:/pythontreenit/puzzlet/aocinput.txt', 'r') as file:
    for line in file:
        fuel = calculate_fuel(int(line))
        
        while True:
            if fuel <= 0:
                fuel = 0
                break
            sum += fuel
            fuel = calculate_fuel(fuel)
print(sum)


# sum1 = 0       
# fuel = calculate_fuel(1969)


# while True:
#     if fuel <= 0:
#         fuel = 0
#         break
#     sum1 += fuel
#     fuel = calculate_fuel(fuel)
# print(sum1)