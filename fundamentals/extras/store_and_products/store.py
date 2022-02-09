from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        removed = self.products.pop(id)
        removed.print_info()
        return self
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_decrease):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_decrease, False)
        return self