import re

def shit():
    with open("C:/pythontreenit/puzzlet/aoc2020_7_input.txt", "r") as filu:
        bags = filu.read().split('\n')

    layer = [x.split()[0]+' '+x.split()[1] for x in list(filter(lambda element: 'shiny gold' in element, bags))]
    print(layer)
    cols = []
    i = 0
    while i < 20:
        for elem in layer:
            
            if elem == 'shiny gold':
                continue
            print(elem)
            cols.append(elem)
            print(cols)
            l = [x.split()[0]+' '+x.split()[1] for x in list(filter(lambda element: elem in element, bags))]
            n = [a for a in l]
            print('n', n)
            cols.extend([a for a in l if a not in cols])
            print('cols on ',cols)
    #         print('l', l)
            layer = cols
            # if len(n) == 0:
            #     return
            # if elem == 'light blue':
            #     return
        i += 1
    return len(set(cols))

print(shit())

        # print('c on vika', c)
        # colors = c
        # #     # print(colors)
        # print(len(c))
        # if elem in c:
        #     continue
        # if len(colors) == 0:
        #     print('ö')
        #     return len(c)
        # if(all(x in c for x in colors)):
        #     print('a')
        #     return len(c)
# def bags():
#     """How many bag colors can eventually contain at least one shiny gold bag?"""
    
#     return bags

# def factorial(bags, col, c):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     print('c on', c)
#     for elem in bags:
        
     
#         # c.extend(colors)
#         print('c on', c)
#         colors = re.split('*( no other | contain [0-9] | bag.| bags.| bags contain )', elem)
#         print(colors)
        # l = [x.split()[0]+' '+x.split()[1] for x in list(filter(lambda element: elem in element, bags))]
        # print('l', l)
        # c.extend([a for a in l if a not in c])
        # print('c on vika', c)
        # colors = c
        # #     # print(colors)
        # print(len(c))
        # if elem in c:
        #     continue
        # if len(colors) == 0:
        #     print('ö')
        #     return len(c)
        # if(all(x in c for x in colors)):
        #     print('a')
        #     return len(c)


    # factorial(bags, colors, c)
# def factorial(bags, colors, c):
#     """This is a recursive function
#     to find the factorial of an integer"""
#     # c = []
#     print('c on', c)
#     for elem in colors:
#         # if elem in c:
#         #     continue
#         # if len(colors) == 0:
#         #     print('ö')
#         #     return len(c)
#         # if(all(x in c for x in colors)):
#         #     print('a')
#         #     return len(c)
     
#         # c.extend(colors)
#         print('c on', c)
#         l = [x.split()[0]+' '+x.split()[1] for x in list(filter(lambda element: elem in element, bags))]
#         print('l', l)
#         c.extend([a for a in l if a not in c])
#  

            
            

  
    # return len(set(res))


# print(bags())