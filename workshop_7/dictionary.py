# Dict - HashMap / Map




en_ka = {
    "hello": "გამარჯობა",
    "bye": "ნახვამდის",
}


print(en_ka["hello"])
en_ka["hello"] = "სალამი"
print(en_ka["hello"])
en_ka.pop("hello")
# del en_ka["hello"]
# del en_ka
print(en_ka)

en_ka["bottle"] = "ბოთლი"
print(en_ka)
# quit()


ka_en = {
    # key : value
    "გამარჯობა": ("hello",),
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

