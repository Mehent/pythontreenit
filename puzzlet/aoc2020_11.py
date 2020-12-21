# import pandas as pd

def shit():
    """If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor."""

    with open("C:/pythontreenit/puzzlet/aoc2020_11_input.txt", "r") as filu:
        rows = filu.read().split('\n')

    i = 0

    while True:
        temp_list = []
        for b, row in enumerate(rows):
            print(b)
            row = [a for a in row]
            for a, seat in enumerate(row):
                ls = []
                if a == 0:
                    if b == 0:
                        ls.extend(rows[b][a:2])
                        ls.extend(rows[b+1][a:2])
                if a == len(row)-1:
                    if b == 0:
                        ls.extend(rows[b][-2:a+1])
                        ls.extend(rows[b+1][-2:a+1])
                if a == 0:
                    if b == len(rows)-1:
                        ls.extend(rows[b][a:2])
                        ls.extend(rows[b-1][a:2])
                if a == len(row)-1:
                    if b == len(rows)-1:
                        ls.extend(rows[b][-2:a+1])
                        ls.extend(rows[b-1][-2:a+1])
                if a == 0:
                    if b > 0 and b < len(rows)-1:
                        ls.extend(rows[b+1][a:2])
                        ls.extend(rows[b][a:2])
                        ls.extend(rows[b-1][a:2])
                if a == len(row)-1:
                    if b > 0 and b < len(rows)-1:
                        ls.extend(rows[b+1][-2:a+1])
                        ls.extend(rows[b][-2:a+1])
                        ls.extend(rows[b-1][-2:a+1])
                if a > 0 and a < len(row)-1:
                    if b > 0 and b < len(rows)-1:
                        ls.extend(rows[b+1][a-1:a+2])
                        ls.extend(rows[b][a-1:a+2])
                        ls.extend(rows[b-1][a-1:a+2])
                if a > 0 and a < len(row)-1:
                    if b == 0:
                        ls.extend(rows[b+1][a-1:a+2])
                        # print('pö')
                        # print(rows[b+1][a-1:a+2])
                        ls.extend(rows[b][a-1:a+2])
                        # print('pi')
                        # print(rows[b][a-1:a+2])
                if a > 0 and a < len(row)-1:
                    if b == len(rows)-1:
                        ls.extend(rows[b][a-1:a+2])
                        ls.extend(rows[b-1][a-1:a+2])
                # print(ls)

                if seat == 'L' and '#' not in ls:
                    row[a] = '#'
                if seat == '#' and ls.count('#') >= 5:
                    row[a] = 'L'

            row = ''.join(row)
            # print(row)
            temp_list.append(row)
        print(temp_list)
        if temp_list == rows:
            break
        rows = temp_list
    count = 0
    for elem in rows:
        for a in elem:
            if a == '#':
                count += 1

    return count



print(shit())