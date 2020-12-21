def customs():
    """docstring"""
    with open("C:/pythontreenit/puzzlet/aoc2020_6_input.txt", "r") as filu:
        data = filu.read().split('\n\n')
    print(data)

    sum = 0
    sum_all = 0
    for ele in data:
        n = len(set(ele.replace('\n','')))
        sum += n
        person = ele.split('\n')
        for a in set(ele.replace('\n','')):
            l = len(person)
            if ele.replace('\n','').count(a) == l:
                sum_all += 1

    return sum, sum_all


print(customs())