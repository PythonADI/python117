menu = {
    "Khinkali": {
        "price": 2,
        "in_stock": True
    },
    "Mtsvadi": {
        "price": 17,
        "in_stock": True
    },
    "French Fries": {
        "price": 6,
        "in_stock": True
    },
    "Rachuli Lobiani": {
        "price": 12,
        "in_stock": True
    },
    "Phkali": {
        "price": 10,
        "in_stock": False
    },
    "Acharuli": {
        "price": 18,
        "in_stock": False
    }
}

[
    ("Mtsvadi", 2),
    ("Khinkali", 40),
]

def take_order():
    order = []
    while True:
        menu_item = input("Choose product(press Q to stop): ")
        if menu_item == "Q":
            print("thank you")
            break
        if menu_item not in menu.keys():
            print(f"we dont have {menu_item}")
            continue
        product = menu[menu_item]
        if not product["in_stock"]:
            print("not in stock")
            continue
        quantity = int(input("How many? "))
        if quantity < 0:
            print("Enter the correct amount")
            continue
        order.append((menu_item, quantity))
    return order

print(take_order())




{
    "total_price": 80,
    "items": [
        ("Mtsvadi", 2),
        ("Khinkali", 40),
    ]
}
def get_total_order():
    pass

