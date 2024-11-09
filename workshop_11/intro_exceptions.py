
def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return

def get_name():
    name = "25" # input("Name")

    if not name.isalpha():
        # print("PLease insert correct name format")
        raise Exception("Please enter correct name format")

    return name

try:
    print(get_name())
except (ValueError, ZeroDivisionError):
    print("Do something")
except Exception:
    print("Something unexpected happened! (please contact developer)")


# for _ in range(30):
#     print("weoifjvwmpiut")

# try:
#     num1 = float(input("Num1: "))
#     num2 = float(input("Num2: "))
# except ValueError:
#     print("Please insert correct number format!")


# try:
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("You can't divide by zero.")
