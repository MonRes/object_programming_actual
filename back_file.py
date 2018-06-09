""" Napisać funkcję odczytującą plik i zapisującą go pod zadaną ścieżkę od tyłu"""

def reverse_file(input_path, output_path):

    with open(input_path, 'rt') as out_file:
        data = out_file.read()

    with open(output_path, 'wt') as out_file:
        out_file.write(data[::-1])

if __name__ == '__main__':
    reverse_file('plik.txt', 'plik_reversed.txt')

