import re


def count_passports():
    """docstring"""
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open("C:/pythontreenit/puzzlet/aoc2020_4_input.txt", "r") as filu:
        passports = filu.read().split('\n\n')

    counter = 0

    for elem in passports:
        lst = re.split('\n| |:', elem)
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        print(res_dct)
        if all(elem in res_dct.keys() for elem in keys):
            if check_byr(res_dct) and check_iyr(res_dct) and check_eyr(res_dct) and check_hgt(res_dct) and check_hcl(res_dct) and check_ecl(res_dct) and check_pid(res_dct):
                counter += 1
    return counter

def check_byr(dct):
    byr = dct.get('byr')
    return byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002

def check_iyr(dct):
    iyr = dct.get('iyr')
    return iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020

def check_eyr(dct):
    eyr = dct.get('eyr')
    return eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030

def check_hgt(dct):
    hgt = dct.get('hgt')
    if 'cm' in hgt:
        return int(hgt.strip('cm')) >= 150 and int(hgt.strip('cm')) <= 193
    if 'in' in hgt:
        return int(hgt.strip('in')) >= 59 and int(hgt.strip('in')) <= 76

def check_hcl(dct):
    hcl = dct.get('hcl')
    return re.match('^#[a-zA-Z0-9]{6,}$', hcl)

def check_ecl(dct):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl = dct.get('ecl')
    return ecl in colors

def check_pid(dct):
    pid = dct.get('pid')
    return pid.isdigit() and len(pid) == 9


print(count_passports())

print(re.split('\n| |:', 'asdfds as\ndf\n\nadf'))