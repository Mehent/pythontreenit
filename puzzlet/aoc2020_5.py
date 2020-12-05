
def boarding():
    """docstring"""
    with open("C:/pythontreenit/puzzlet/aoc2020_5_input.txt", "r") as filu:
        bpasses = filu.read().split('\n')

    ids = []
    codelist = [[n for n in x] for x in bpasses]

    for elem in codelist:
        rows = [a for a in range(128)]
        columns = [a for a in range(8)]
        for item in elem:
            if item == 'F':
                rows = rows[:len(rows)//2]
            if item == 'B':
                rows = rows[len(rows)//2:]
            if item == 'R':
                columns = columns[len(columns)//2:]
            if item == 'L':
                columns = columns[:len(columns)//2]

        ids.append(rows[0] * 8 + columns[0])
        id = find_id(ids)
    return max(ids), id

def find_id(lst_of_ids):
    num_list = sorted(lst_of_ids)
    c = num_list[0]
    for elem in num_list:
        if elem == c+2:
            return elem-1
        c = elem

print(boarding())
