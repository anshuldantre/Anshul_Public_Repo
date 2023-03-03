# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
class Product:
    def __init__(self, product_name, price, category, product_id):
        self.product_name = product_name
        self.price = price
        self.category = category
        self.product_id = product_id

# Let's give some methods to our Product class:
# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. 
# If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change) / 100
        elif is_increased == False:
            self.price -= (self.price * percent_change) / 100
        return self

# print_info(self) - print the name of the product, its category, and its price.
    def print_info(self):
        print(f'The product id {self.product_id} having name = {self.product_name} is sold for a price of ${self.price} under {self.category} category')
        return self