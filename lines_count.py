"""stworzyć słownik gdzie linia o długości 10 wystąpiła n razy"""

with open('plik.txt') as my_file: ## wczytanie wszystkich linii z pliku na raz, zachowuje znak końca linii
    lines = my_file.readlines()

    lines_hist = {}
    for line in lines:
        line2 = line.rstrip('\r\n')
        lines_hist[len(line2)] = lines_hist.get(len(line2), 0) + 1
    print(lines_hist)