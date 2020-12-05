import re


def count_passwords(right, down):
    """docstring"""
    maplist = []

    with open("C:/pythontreenit/puzzlet/aoc2020_3_input.txt", "r") as filu:
        for line in filu:
            maplist.append(line.strip('\n').rstrip())


    row_length = len(maplist[0])
    negative_ind = 0-row_length

    counter_x = 0

    location_row = 0
    location_col = negative_ind
    while location_row < len(maplist)-1:
        if (row_length -1) - location_col < right:
            location_col = right - ((row_length) - location_col)
        else:
            location_col += right
        location_row += down
        if maplist[location_row][location_col] == '#':
            counter_x += 1

    return counter_x



print('kuusia',count_passwords(1, 1))
print('kuusia',count_passwords(3, 1))
print('kuusia',count_passwords(5, 1))
print('kuusia',count_passwords(7, 1))
print('kuusia',count_passwords(1, 2))
print(66*200*76*81*46)