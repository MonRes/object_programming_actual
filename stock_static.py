import copy

class Stock:

    def __init__(self, initial):
        self.products = copy.deepcopy(initial)


    def resupply(self, product, count):

        if count <=0:
            raise ValueError('Can ressuply only with possitive count')

        self.products[product] = self.products.get(product, 0) + count #przypisanie nie pobranie



    def withdraw(self, product, count):
        if count <=0:
            raise ValueError('Can ressuply only with possitive count')
        if product not in self.products:
            raise ValueError('Unknown product ' + product)
        if self.products[product] < count:
            raise ValueError('Insufficient number of items in stock')

        self.products[product] -= count

    def available_items(self):
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items

    def save(self, file_obj): #zapisze stock produkt, ilość do pliku
        for product, count in self.products.items():
            file_obj.write(product + ',' + str(count) + '\n')

    def save2(self, file_obj):
        lines = [prod + ',' + str(count) + '\n'
                 for prod, count in self.products.items()]
        file_obj.writelines(lines)



    @staticmethod #odczytuje plik, inicjalizuje i zwraca
    def load(file_obj):
        data = {}
        for line in file_obj:
            record = line.rstrip('\r\n').split(',')
            data[record[0]] = int(record[1])
        return Stock(data)

    @staticmethod ##ona się wywoła bez printa po samym Stock.foo() jest takie samo bez znaczenia czy Stock czy inna instaancja
    def foo(a):
        print('Static method called!', a)


# products = {'orange': 2, 'bananas': 3} #przypisanie obiektu do zmiennej nie tworzy jego kopii, nie robić tak
stock = Stock({'orange': 2, 'bananas': 3})
stock.resupply('orange', 2)


print(stock.products)
#products['orange'] = -500 # tak nie robić
print((stock.products))

with open('magazyn.csv', 'wt') as data_file:
    stock.save(data_file)

with open('magazyn2.csv', 'wt') as data_file:
    stock.save2(data_file)

with open ('magazyn.csv', 'rt') as data_file:
    stock2 = Stock.load(data_file)
    print(stock2.available_items())

#Stock.foo('a') #print stock.foo nie równa się Stock.foo, przy @staticmethod to jest to samo, bo nie próbuje się bindować