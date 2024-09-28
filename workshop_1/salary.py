import random
money = 0
salary = 2500
tax = 0.2
net_salary = salary * (1 - tax)

sandwich_price = 10
bills = 500

money += net_salary
print("I got paid ", net_salary, "$.")
print("I have ", money, "$ right now.")
# money = money - 10
money -= sandwich_price
print("I bought a sandwich for ", sandwich_price, "$ and now I have ", money, "$ left.")
money -= bills
print("I paid my bills ", bills, "$ and now I have ", money, "$ left.")
money *= (random.randint(0, 200) / 100)
print("I have ", money, "$ right now.")