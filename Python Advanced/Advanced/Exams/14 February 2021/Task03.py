from collections import deque


def stock_availability(inventory, order, *args):
    other_parameters = deque(args)

    if order == "delivery":
        while other_parameters:
            inventory.append(other_parameters.popleft())
        return inventory

    elif order == "sell":
        if other_parameters:
            if type(other_parameters[0]) == int:
                return inventory[other_parameters[0]:]
            else:
                for current_parameter in other_parameters:
                    if current_parameter in inventory:
                        inventory = [value for value in inventory if value != current_parameter]
                return inventory

        else:
            inventory.pop(0)
            return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
