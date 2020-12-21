from itertools import combinations
import numpy
from functools import reduce


def joltage(data, builtin):
    """Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
    In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag"""
    # differences = [1, 1, 1, 2, 3, 2, 3, 1]

    differences = []
    previous = 0

    data.sort()

    for elem in data:
        # print(elem)
        if elem > previous and elem <= previous+3:
            differences.append(elem-previous)
            previous = elem

    differences.append(3)


    # values = [1, 3, 4, 6, 9, 10, 11, 12, 15]
    # data.append(max(sdata)+3)
    
    # data.append(0)
    data.sort(reverse=True)
    differences.sort(reverse=True)
    print(data)
    possib = []

    for i, elem in enumerate(data):
        ls = [a for a in data[i+1:i+4] if elem -a <= 3]
        print(data[i+1:i+4])
        print(ls)
       
        if len(ls) > 0:
             possib.append(len(ls))
    print(possib)
    result1 = reduce((lambda x, y: x * y), possib)
    print(result1)
    result = 1
    for x in possib:
         result = result * x 
    print(result) 
    # count = 0
    # ls = []
    
    
    # for a in range(3):
    #     for i in range(a, len(data)-3, 3):
    #         if data[i:i+3][-1]-data[i:i+3][0] <= 3:
    #             print(data[i:i+3])
    #             # print(data[i:i+3][0])
    #             count += 1
    #     ls.append(count)
    #     count = 0
            
    # potenssit = []
    # for ele in ls:
    #     print(ele)
    #     potenssit.append(ele**ele)
    # print(potenssit)
    # print(sum(set(potenssit)))


    # # What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
  
   
    # print(2**48)


    # print(differences.count(1))
    # print(differences.count(3))
    # print(differences.count(1)-22)
    return differences.count(1)*differences.count(3)


data = []
with open("C:/pythontreenit/puzzlet/aoc2020_10_input.txt", "r") as filu:
    for line in filu:
        data.append(int(line))
builtin_adapter = sorted(data)[-1]+3
print(joltage(data, builtin_adapter))