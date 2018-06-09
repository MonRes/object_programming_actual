"""otwieranie i zamykanie pliku"""

my_file = None #inaczej jeśli to pominiemy, to w finally nie będzie utworzy plik
try:
    my_file = open('plik.txt', 'rt') #domyślnie argument rt czyli odczyt i traktuj jako txt
    data = my_file.read()
    print(data)
except OSError as err:
    print('Error: ', str(err))
finally:
    if my_file is not None:
        print('Zamykam')
        my_file.close()

#jeśli nie ma takiego pliku dostajemy FileNotFoundError

#konstrukcja do tego co powyżej

try:
    with open('plik2.txt') as my_file: #otwiera plik i nazywa zmienną plikową jako my_file. w open mogą być argumenty
        print(my_file.read()) #zamykanie pliku samo się zrobi
except OSError as err:
    print(err)

##WCZYTYWANIE LINII Z PLIKU

with open('plik.txt') as my_file: ## wczytanie wszystkich linii z pliku na raz, zachowuje znak końca linii
    lines = my_file.readlines()
    print(lines)

with open('plik.txt') as my_file: # wypisanie linii przez iterowanie po zawartości pliku również zachowuje znak końca linii ale inaczej
    for line in my_file:
        print(line)

##usuwanie znaków za pomoca metody strip
text = 'some text'
print(text.rstrip('\r\n')) #usuwamy te znaki dopóki nie napotka znaku, którego ma nie obcinać