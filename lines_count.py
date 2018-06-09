"""stworzyć słownik gdzie linia o długości 10 wystąpiła n razy"""

with open('plik.txt') as my_file: ## wczytanie wszystkich linii z pliku na raz, zachowuje znak końca linii
    lines = my_file.readlines()

    lines_hist = {}
    for line in lines:
        line2 = line.rstrip('\r\n')
        lines_hist[len(line2)] = lines_hist.get(len(line2), 0) + 1
    print(lines_hist)


## druga opcja z funkcją

def lines_histogram(input_path):
    result = {}

    with open(input_path, 'rt') as in_file:
        for line in in_file:
            stripped = line.rstrip('\r\n')
            result[len(stripped)] = result.get(len(stripped), 0) + 1
    return result

if __name__ == '__main__':
    path = input('Podaj ścieżke: ')
    try:
        print(lines_histogram(path))
    except OSError as err:
        print(err)

## opcja najbardziej poprawna

def lines_histogram2(input_file):
    result = {}
    for line in input_file:
        key = len(line.rstrip('\r\n'))
        result[key] = result.get(key, 0) + 1
    return result

if __name__ == '__main__':
    path = input('Podaj ścieżke: ')
    try:
        print(lines_histogram(path))
    except OSError as err:
        print(err)

    try:
        with open(path, 'rt') as in_file:
            print(lines_histogram2(in_file))
    except OSError as err:
        print(err)