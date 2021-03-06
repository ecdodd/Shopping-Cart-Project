import code
import operator  # code.interact(local=locals())

products_ids = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # Products based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(len(products))

#def product_ids(product_id):
#    return [product for product in products if product["id"] == product_id] # list comprehension for the win. so helpful.

while True:
    product_id = input("Please input a valid product identifier, or 'DONE' if there are no more items:")
    if product_id == "DONE":
        print("THANKS ALL DONE HERE")
        break
    else:
        print("THE PRODUCT IDENTIFIER IS: " + str(product_id))
        product_ids.append(int(product_id))

def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0] # because the line above gives us a list and we want to return a single item.

#print("OUTSIDE THE LOOP")
#print(product_ids)
#
code.interact(local=locals())

product_ids = [1, 8, 6, 16, 6]

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", product_ids)

#TODO: peform product look-ups here!

def product_lookup():
    word = raw_input("Word to lookup: ")
    for product_id in products:
        if product[0] == word:
            print (fruit[0], ":", fruit[1], "\n")
            return
    print("That word does not exist in the dictionary")
product_lookup()


#for i in product_ids:
#    print(i)
#    if i == 8:
#        code.interact(local=locals())

##for product in products:
##    price_usd = ' (${0:.2f})'.format(product["price"])
##    print(" + " + product["name"] + price_usd)
