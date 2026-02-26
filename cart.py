class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def show_product(self):
        print("Name:", self.name, "\nPrice:", self.price, "\nQuantity:", self.quantity)
        
    def total_price(self):
        print("Total price for", self.name, ":", self.price * self.quantity)        