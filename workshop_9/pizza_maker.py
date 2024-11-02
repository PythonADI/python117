def make_pizza(*toppings, size):
    pizza = ["Sauce"]
    for topping in toppings:
        pizza.append(topping)
    print(f"You have chosen following toppings: {pizza} / {size}cm")



def build_profile(first_name, last_name, **extra):
    print(f"{extra = }")
    user = {
        "first_name": first_name,
        "last_name": last_name
    }
    user.update(extra)
    return user

make_pizza("Pepperoni", "Mozzarela", "Cheese", "Goat Cheese", size=33)
print(build_profile("George", "Washington", age = 17, wife = "Theresa", daughter = "Margaret"))
print(build_profile("Theodor", "Roosevelt", pet = "dog"))
print(build_profile("Teddy", "Roosevelt"))

