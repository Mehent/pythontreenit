def rainrisk():
    """docstring"""
    with open("C:/pythontreenit/puzzlet/aoc2020_12_input.txt", "r") as filu:
        data = filu.readlines()
    coord = []
    for ele in data:
        coord.append([ele[:1], int(ele[1:].rstrip())])
    # print(coord)

    ilmansuunnat = ('N', 'E', 'S', 'W')
    facing = 'E'
    horiz = 0
    vertic = 0
    for ele in coord:
        if ele[0] == 'N':
            vertic += ele[1]
        if ele[0] == 'E':
            horiz += ele[1]
        if ele[0] == 'S':
            vertic -= ele[1]
        if ele[0] == 'W':
            horiz -= ele[1]
        if ele[0] == 'L':
            ind = ilmansuunnat.index(facing)
            i = 0
            while i < ele[1]/90:
                if ilmansuunnat.index(facing) == 0:
                    ind = 3
                else:
                    ind = ilmansuunnat.index(facing) -1
                i += 1
                facing = ilmansuunnat[ind]
        if ele[0] == 'R':
            ind = ilmansuunnat.index(facing)
            i = 0
            while i < ele[1]/90:
                if ilmansuunnat.index(facing) == 3:
                    # print('testi')
                    ind = 0
                else:
                    ind = ilmansuunnat.index(facing) + 1
                # print('ind on')
                # print(ind)
                i += 1
                facing = ilmansuunnat[ind]
        if ele[0] == 'F':
            if facing == 'N':
                vertic += ele[1]
            if facing == 'E':
                horiz += ele[1]
            if facing == 'S':
                vertic -= ele[1]
            if facing == 'W':
                horiz -= ele[1]
        # print(horiz)
        # print(vertic)
        # print(facing)

    print(horiz)
    print(vertic)




    # return facing
    return abs(horiz) + abs(vertic)
        





print(rainrisk())