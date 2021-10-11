animal_class = str(input())

if animal_class == "dog":
    print("mammal")
elif animal_class == "crocodile" or animal_class == "tortoise" or animal_class == "snake":
    print("reptile")
else:
    print("unknown")
