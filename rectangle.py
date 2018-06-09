"""Implementation of the Rectangle class"""

class Rectangle: #w poprzednich wersjach Rectangle(object)

    """A Rectangle.

    Args:
        width: width of the rectangle
        height: height of the rectangle
    Both width and height should be positive numbers"""

    x = 10 # stała, której mogą używać wszystkie obiekty danej klasy. Atrybuty dla wszystkich obiektów tylko w inicie

    def __init__(self, width, height): #tworzenie inicjalizatorów, podkreślniki mówią o tym, że jest metodą specjalną
        if width <= 0:
            raise ValueError ('Width has to be positive')
        if height <= 0: #po ustawieniu height i width można uzyć self.width, ale lepiej tak
            raise ValueError ('Height has to be positive')
        self.width = width #ustaw atrybut selfa - width na width
        self.height = height # self mówi zainicjalizuje ten obiekt na którym działamy, po wysokości i szerokości, przypisanie atrybutowi dowolną wartość

#init co ten obiekt ma za atrybuty (kolor, wysokość itp), zwykłe metody to co ten obiekt robi

    def area(self):
        """Computes the area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Computes the perimeter of rectangle"""
        return 2 * (self.height + self.width)

    def draw(self):
        pass #wyrysowanie gwiazdkami, pusty w środku

rect = Rectangle(100, 20) # ten rect to self
print('Pole', rect.area()) #wywołujemy bez argumentu bo nie było, dlatego nawiasy bo funkcja
print('Obwód', rect.perimeter())
print('Wysokość: ', rect.height)
print('Szerokość: ', rect.width)
Rectangle(-1, 2)
