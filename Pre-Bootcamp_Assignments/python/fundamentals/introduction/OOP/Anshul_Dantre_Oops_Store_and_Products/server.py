from product import Product
from store import Store
# Assignment: Store & Products
# Create a Store class with 2 attributes
# Create a Product class with 3 attributes
# Add the print_info method to the Product class
# Add the update_price method to the Product class
# Add the add_product method to the Store class
# Add the sell_product method to the Store class
# NINJA BONUS: Modularize your code into 3 separate files

# Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
store1 = Store("Walmart")
store2 = Store("Costco")
print(store1.name)

Product1 = Product("Milk",13,"Dairy", 11)
Product2 = Product("Eggs",8,"Dairy", 12)

Product3 = Product("Rice",20,"Grains", 21)
Product4 = Product("Lentils",7,"Grains", 22)
Product5 = Product("Beans",9,"Grains", 23)

Product.print_info(Product1)
Product.print_info(Product2)
Product.print_info(Product3)
Product.print_info(Product4)
Product.print_info(Product5)

store1.product_list.append(Product1)
store1.product_list.append(Product2)

store2.product_list.append(Product3)
store2.product_list.append(Product4)
store2.product_list.append(Product5)

print("---")
print(store1)
print("---")
print(store1.product_list)
print("---")
for i in store1.product_list:
    print(f'Product = {i.product_name} for ${i.price} under {i.category} ')
print("---")

# NINJA BONUS: Add the inflation method to the Store class
store1.inflation(25)
for i in store1.product_list:
    print(f'Product = {i.product_name} for ${i.price} under {i.category} ')
print("---")

# NINJA BONUS: Add the set_clearance method to the Store class
store2.set_clearance("Grains", 15)
for i in store2.product_list:
    print(f'Product = {i.product_name} for ${i.price} under {i.category} ')
print("---")

# SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
store1.sell_product(11)
for i in store1.product_list:
    print(f'Product = {i.product_name} for ${i.price} under {i.category} ')
print("---")

store2.sell_product(23)
for i in store2.product_list:
    print(f'Product = {i.product_name} for ${i.price} under {i.category} ')
print("---")