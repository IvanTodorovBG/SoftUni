import re

data = input()
total_income = 0

while data != "end of shift":
    pattern_customer = r"\%(?P<customer>[A-Z][a-z]+)\%"
    customer = re.finditer(pattern_customer, data)
    is_customer = bool([c.group(0) for c in customer])

    pattern_product = r"\<(?P<product>[0-9a-zA-Z\_]+)\>"
    product = re.finditer(pattern_product, data)
    is_product = bool([p.group(0) for p in product])

    pattern_count = r"\|(?P<count>[0-9]+)\|"
    count = re.finditer(pattern_count, data)
    is_count = bool([cnt.group(0) for cnt in count])

    pattern_price = r"(?P<price>[0-9]+\.?[0-9]+)\$"
    price = re.finditer(pattern_price, data)
    is_price = bool([pr.group(0) for pr in price])

    if is_customer and is_product and is_count and is_price:

        customer_dict = {}
        for c in re.finditer(pattern_customer, data):
            customer_dict = c.groupdict()

        product_dict = {}
        for p in re.finditer(pattern_product, data):
            product_dict = p.groupdict()

        count_dict = {}
        for cnt in re.finditer(pattern_count, data):
            count_dict = cnt.groupdict()

        price_dict = {}
        for pr in re.finditer(pattern_price, data):
            price_dict = pr.groupdict()

        total_product_price = int(count_dict['count']) * float(price_dict['price'])
        total_income += total_product_price

        print(f"{customer_dict['customer']}: {product_dict['product']} - {total_product_price:.2f}")

    data = input()

print(f"Total income: {total_income:.2f}")