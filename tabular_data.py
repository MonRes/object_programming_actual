import copy

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {}
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
        # wyrażenie słownikowe self._columns={name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self._columns):
            raise ValueError('Column names have to be uniqe')
        self._rows = [] #możemy definiować ile chcemy danych a nie musimy ich mieć w atrybucie metody, column names jest wymagane

# taki zapis _rows = to pole prywatne

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError('Invalid row number: ', row_no)
        return self._rows[row_no]


    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError('Unknow column: ', col_name)
        idx = self._columns[col_name]
        # return [row[idx] for row in self.rows] - wyrażenie listowe dla pętli poniżej
        values = []
        for row in self._rows:
            values.append(row[idx])
        return values


    def append(self, new_row):
        if len(new_row) != len(self._columns):
            raise ValueError('to many elements')
        self._rows.append(list(new_row))

    def rows_count(self):
        return len(self._rows)

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __len__(self): #jak ktoś wywoła len na mnie to ty wywołaj len
        return len(self._rows)

    def __str__(self): #zmieniamy całą tabelkę na str
        return str(self._rows)

table = TabularData(['name', 'surname', 'age'])
table.append(['John', 'Doe', 30])
table.append(['Joe', 'Dragon', 20])
table.append(['Ann', 'Philips', 10])
table.append(['Christopher', 'Carmen', 12])
print(table._rows)
print(table.get_column('name'))
print(table.get_row(0))
print(table.column_names)
print(table._rows)
print(len(table))
print(str(table))
