# Dict - HashMap / Map

ka_en = {
    # key : value
    "გამარჯობა": ("hello"),
    "ნახვამდის": ("goodbye", "bye", "see you"),
    "როგორ ხარ?": ("how are you?",),
    "ბოთლი": (),
}

# print(ka_en["გამარჯობა"])
# print(ka_en["ნახვამდის"])
# print(ka_en["როგორ ხარ?"])

for key, value in ka_en.items():
    print(key, value, type(value))

# print("Only keys")
print("Georgian words: ")
for key in ka_en:  # ka_en.keys()
    # print(key, ka_en[key])
    print(key)

# print("Only values")
print("English Woords: ")
for value in ka_en.values():
    print(value)
