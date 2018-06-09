import copy
data = { 'a': 100, 'b': 10}
print(data['a'])
print(data.get('c', 300)) # nie ma klucza c więc zwracam 300 ale nie dodaje do listy, dlatego przypisujemy ją od razu do klucza tak jak w stocku
print(data)

inner = {1: 'foo', 2: 'bar'}
outer = {'a': inner, 'b': 2}
outer2 = copy.deepcopy(outer) # za każdym razem gdy napotyka na słownik, tworzy jego kopię
#outer2 = dict(outer) #tworzona kopia tylko pierwszego słownika, nowy słownik który ma takie same klucze i wartości //kopia płytka
print(outer)
print(outer2)
outer['b'] = 3
print(outer)
print(outer2)
outer2['a'][1] = 'baz'
print(outer)
print(outer2)