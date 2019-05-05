class Product:
    next_id = 1

    def __init__(self, name = "", description = "", price = 0, quantity = 0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.next_id += 1 

    @property
    def get_id(self):
        return self.next_id

    def get_total_sum(self):
        return self.price * self.quantity

class Shoping(Product):
    zakupki = {}

    def __init__(self):
        super().__init__('Product')

    def add_new_product(self, new_product):
        Shoping.zakupki[new_product.get_id] = new_product 
    def remove_product(self, product_id):
        del Shoping.zakupki[product_id]
    def change_product_quantity(self, product_id, new_quantity):
        Shoping.zakupki[product_id.quantity] = new_quantity
    
    def print_receip(self):
        sum = 0
        for key in Shoping.zakupki:
            print(f'''{Shoping.zakupki[key].name} - {Shoping.zakupki[key].price},
            {Shoping.zakupki[key].quantity},
            {Shoping.zakupki[key].get_total_sum()}'''
                  .replace('\n', ""))
            """
            print("{} - {}, {}, {}" .format(Shoping.zakupki[key].name, 
                Shoping.zakupki[key]).price, Shoping.zakupki[key].quantity, 
                Shoping.zakupki[key].get_total_sum())
            """
        sum += Shoping.zakupki[key].get_total_sum()
        print("Łączna kwota paragonu: {}" .format(sum))



produkt1 = Product("Woda", "Napoje", 2, 3)
produkt2 = Product("Gruszka", "Owoc", 12, 2)
produkt3 = Product("Kawa", "Napoje", 10, 20)

koszyk = Shoping()
koszyk.add_new_product(produkt1)
koszyk.add_new_product(produkt2)
koszyk.add_new_product(produkt3)

koszyk.print_receip()








