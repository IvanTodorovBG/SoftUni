given_products = input().split(" ")
search_products = input().split(" ")

stock = {}

for current_index in range(0, len(given_products), 2):
    key = given_products[current_index]
    value = given_products[current_index + 1]
    stock[key] = int(value)

for current_item in search_products:
    if current_item in stock:
        print(f"We have {stock[current_item]} of {current_item} left")
    else:
        print(f"Sorry, we don\'t have {current_item}")

