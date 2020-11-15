import sys
import random
import argparse
import statistics
import operator

class Koodauskoe:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='This is calculation program')
        self.parser.add_argument('filename', help='tiedoston nimi')
        self.parser.add_argument('laskutoimitus', help='sum, avg or median')
        self.parser.add_argument('comparison', nargs="?", help='gt, lt or eq')
        self.parser.add_argument('number', nargs="?", type=int)

    def get_args(self):
        args = self.parser.parse_args()
        return args

    def read_file(self, args):
        """Käsitellään tiedosto: viedään numerot listaan. Jos tiedostoa ei ole,
        luodaan sellainen sisältöineen ja informoidaan tästä käyttäjää
        """
        list_of_numbers = []
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
        return list_of_numbers

    def count(self, args):
        """Käsitellään pakollinen argumentti, joka määrää suoritettavan laskutoimituksen
        tallennetaan result-muuttujaan toimituksen tulos ja printataan
        """
        list_of_numbers = self.read_file(args)
        result = 0
        if args.laskutoimitus == 'sum':
            result = sum(list_of_numbers)
            print('Summa on:',result)
        elif args.laskutoimitus == 'avg':
            print('Keskiarvo on:',result)
        elif args.laskutoimitus == 'median':
            result = statistics.median(list_of_numbers)
            print('Mediaani on: ',result)
        else:
            raise self.parser.error("arg 'laskutoimitus' must be given as 'sum', 'avg' or 'median'!")
        return result

    def optional_args(self, args, result):
        """Käsitellään valinnaiset argumentit, jolla määritetään millainen vertailu tulokselle suoritetaan
        ja mitä lukua vastaan. Comp-muuttujaan tallentuu True tai False, jonka perusteella valitaan viesti käyttäjälle
        """
        if args.comparison and not args.number:
            self.parser.error('number argument is required when comparison arg is set.')

        comp = None
        vertailu = ''

        if args.comparison:
            if args.comparison == 'gt':
                comp = operator.gt(result, int(args.number))
                vertailu = 'suurempi'
            elif args.comparison == 'lt':
                comp = operator.lt(result, int(args.number))
                vertailu = 'pienempi'
            elif args.comparison == 'eq':
                comp = operator.eq(result, int(args.number))
                vertailu = 'yhtä suuri'
            else:
                raise self.parser.error("comparison argument is not valid. Use 'gt', 'lt' or 'eq'.")

        if comp:
            print(f'{result} on {vertailu} kuin {args.number}')
        else:
            print(f'{result} ei ole {vertailu} kuin {args.number}')


if __name__ == '__main__':
    K = Koodauskoe()
    a = K.get_args()
    K.read_file(a)
    r = K.count(a)
    K.optional_args(a, r)









