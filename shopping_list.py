class Shopper:
    stores = []

    def add_list(self):
        self.stores.append(store)
        print(stores)

class ShoppingList:
    products = []

    def __init__(self, store):
        self.store = store
        print('Shopping list created')

    def add(self, item):
        self.products.append(item)

    def show(self):
        print(self.store)
        print(self.products)

fiesta = ShoppingList('Fiesta')
fiesta.add('Milk')
fiesta.add('Soda')
fiesta.add('Fish')
fiesta.show()

walmart = ShoppingList('Walmart')
walmart.add('Paper')
walmart.add('Napkins')
walmart.add('Plates')
walmart.add('Chips')
walmart.show()

sams = ShoppingList("Sam's Club")
sams.add('Chicken')
sams.add('Beef')
sams.add('Eggs')
sams.add('Sugar')
sams.add('Salt')
sams.add('Pepper')
sams.add('Honey')
sams.show()
