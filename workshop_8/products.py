products = [
    {"name": "apple", "price": 3, "quantity": 14},
    {"name": "carrot", "price": 6, "quantity": 27},
    {"name": "cabbage", "price": 9, "quantity": 15}
]

most_expensive_product = products[0]

for product in products:
    if most_expensive_product["price"] < product["price"]:
        most_expensive_product = product

print(most_expensive_product)


