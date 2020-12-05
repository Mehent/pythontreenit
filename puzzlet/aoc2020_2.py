import re


def count_passwords():
    """docstring"""
    wordlist = []
    # wordlist = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
    with open("C:/pythontreenit/puzzlet/aoc2020_2_input.txt", "r") as filu:
        for word in filu:
            wordlist.append(word)

    counter1 = 0
    counter2 = 0

    for elem in wordlist:
        parts = elem.split(': ')
        word = parts[1]
        conditions = parts[0].split()
        numbers = conditions[0].split('-')
        minim = int(numbers[0])
        maxim = int(numbers[1])
        letter = conditions[1]

        if word.count(letter) >= minim and word.count(letter) <= maxim:
            counter1 += 1
        if word[minim-1] == letter and word[maxim-1] != letter or word[minim-1] != letter and word[maxim-1] == letter:
            counter2 += 1

    return counter1, counter2


print(count_passwords())