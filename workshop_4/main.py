premium_check = input("Premium Customer? (yes/no): ")
if premium_check == "yes":
    premium = True
else:
    premium = False

numbers = []

amount_of_numbers = int(input("How many phone numbers do you want to add to the list? "))

while len(numbers) != amount_of_numbers:
    numbers.append(input("Enter phone number: "))

country_code = input("\nEnter country code (don't use +): ")

for i, phone_number in enumerate(numbers):
    numbers[i] = f'+{country_code} {phone_number}'

# for i in range(len(numbers)):
#     numbers[i] = f'+{country_code} {numbers[i]}'

print("\nSending messages!")

for phone_number in numbers:
    print(f"Sending message to: {phone_number}")

cost_for_message = 0.10

total_cost = len(numbers) * cost_for_message

print(f"\nTotal cost of sending messages: ${total_cost}")

if premium and len(numbers) > 5:
    discount = 0.2
else:
    discount = 0


after_discount_price = total_cost - total_cost * (1 - discount)
print(f"Total cost after discount: ${after_discount_price}")
