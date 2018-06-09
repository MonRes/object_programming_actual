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


# products = {'orange': 2, 'bananas': 3} #przypisanie obiektu do zmiennej nie tworzy jego kopii, nie robić tak
stock = Stock({'orange': 2, 'bananas': 3})
stock.resupply('orange', 2)

print(stock.products)
#products['orange'] = -500 # tak nie robić
print((stock.products))