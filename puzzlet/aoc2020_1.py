from itertools import combinations


def find_numbers(subsum, how_many_to_sum):
    """docstring"""
    arr = []
    with open("C:/pythontreenit/puzzlet/aoc2020_1_input.txt", "r") as filu:
        for num in filu:
            arr.append(int(num))
    result = [c for c in combinations(arr, how_many_to_sum) if sum(c) == subsum]
    if result:
        res = 1
        for ele in result[0]:    # otetaan eka elementti, koska tuple listan sisällä
            res *= ele
        return res

print(find_numbers(2020, 2))
