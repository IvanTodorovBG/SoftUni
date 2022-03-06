n = int(input())

for _ in range(n):
    text = input()

    start_name = text.find("@") + 1
    end_name = text.find("|")
    name = text[start_name:end_name]

    start_age = text.find("#") + 1
    end_age = text.find("*")
    age = text[start_age:end_age]

    print(f"{name} is {age} years old.")

