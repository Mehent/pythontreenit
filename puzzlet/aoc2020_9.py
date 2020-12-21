from itertools import combinations


def xmas(data):
    starter_ind = 0
    end_ind = 25
    
    for i in range(25,len(data)):
        l_slice = data[starter_ind:end_ind]
        sum_res = int(data[i])
        print(sum_res)
        result = [c for c in combinations(l_slice, 2) if sum(c) == sum_res]

        if result:
            starter_ind += 1
            end_ind += 1
        else:
            return sum_res

def xmas_2(data, s):
    for i in range(2,len(data)+1):
        starter_ind = 0
        end_ind = i
        for a in range(len(data)):
            l_slice = data[starter_ind:end_ind]
            result = [c for c in combinations(l_slice, i) if sum(c) == s]
            if result:
                return sorted(result[0])[0]+sorted(result[0])[-1]
            else:
                starter_ind += 1
                end_ind += 1
        
data = []
with open("C:/pythontreenit/puzzlet/aoc2020_9_input.txt", "r") as filu:
    for line in filu:
        data.append(int(line))

res = xmas(data)
print(xmas_2(data, res))