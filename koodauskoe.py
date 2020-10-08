import sys
import random
import argparse
import statistics
import operator

parser = argparse.ArgumentParser(description='This is calculation program')
parser.add_argument('filename', help='tiedoston nimi')
parser.add_argument('laskutoimitus', help='sum, avg or median')
parser.add_argument('optional_argument', nargs="?", help='gt, lt or eq')
parser.add_argument('number', nargs="?", type=int)
args = parser.parse_args()

list_of_numbers = []
#Käsitellään tiedosto: viedään numerot listaan. Jos tiedostoa ei ole,
# luodaan sellainen sisältöineen ja informoidaan tästä käyttäjää
try:
    with open(args.filename, 'r') as file:
        for line in file:
            list_of_numbers.append(int(line.strip('\n')))
except FileNotFoundError:
    with open(args.filename, 'a+') as filu:
        print(f'File with given name not found, new file named {args.filename} with random numbers created')
        for i in range(10):
            random_number = str(random.randint(1, 999))
            filu.write(random_number+'\n')
#Käsitellään pakollinen argumentti, joka määrää suoritettavan laskutoimituksen
#tallennetaan result-muuttujaan toimituksen tulos ja printataan
result = 0
if args.laskutoimitus == 'sum':
    result = sum(list_of_numbers)
    print('Summa on:',result)
elif args.laskutoimitus == 'avg':
    result = sum(list_of_numbers) / len(list_of_numbers)
    print('Keskiarvo on:',result)
elif args.laskutoimitus == 'median':
    result = statistics.median(list_of_numbers)
    print('Mediaani on: ',result)
else:
    print('argument is not valid. Program can calculate \'sum\', \'avg\' or \'median\'.')
#Käsitellään valinnaiset argumentit, jolla määritetään millainen vertailu tulokselle suoritetaan
#ja mitä lukua vastaan. Comp-muuttujaan tallentuu True tai False, jonka perusteella valitaan viesti käyttäjälle
comp = None
vertailu = ''
if args.optional_argument != None:
    if args.optional_argument == 'gt':
        comp = operator.gt(result, int(args.number))
        vertailu = 'suurempi'
    elif args.optional_argument == 'lt':
        comp = operator.lt(result, int(args.number))
        vertailu = 'pienempi'
    elif args.optional_argument == 'eq':
        comp = operator.eq(result, int(args.number))
        vertailu = 'yhtä suuri'
    else:
        print('argument is not valid. Use \'gt\', \'lt\' or \'eq\'.')
if vertailu:
    if comp:
        print(f'{result} on {vertailu} kuin {args.number}')
    else:
        print(f'{result} ei ole {vertailu} kuin {args.number}')








