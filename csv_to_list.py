## rozwiązanie Konrada, do csv_file

def csv_to_list(csv_file):
    return [line.rstrip('\r\n').split(',') for line in csv_file] #samo wyrażenie listowe które wypisuja tablice, ale bez wyjątku



def csv_to_list2(csv_file):
    expected_len = None
    result = []

    for line in csv_file:
        record = line.rstrip('\r\n').split(',')
        if expected_len is None: #warunek spełniony będzie tylko raz
            expected_len = len(record)
        elif len(record) != expected_len:
            raise ValueError('Malformed CSV file.')
        result.append(record)
    return result

def csv_to_list3(csv_file):
    result = [csv_file.readline().rstrip('\r\n').split(',')]
    for line in csv_file:
        record = line.rstrip('\r\n').split(',')
        if len(record) != len(result[0]):
            raise ValueError('Malformed CSV file')
        result.append(record)
    return result

if __name__ == '__main__':
    with open('dane.csv') as csv_file:
        print(csv_to_list2(csv_file))