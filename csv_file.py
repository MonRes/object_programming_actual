##mój sposób

def csv_read(input_file):

    with open(input_file) as my_file:
        lines = my_file.readlines()

        rows = []
        for line in lines:
            line2 = line.rstrip('\r\n')
            rows.append(line2.split(','))
        return rows

if __name__ == '__main__':
    path = input('Podaj ścieżke: ')
    try:
        print(csv_read(path))
    except OSError as err:
        print(err)


