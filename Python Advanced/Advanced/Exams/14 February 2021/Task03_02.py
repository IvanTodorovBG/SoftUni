from collections import deque


def stock_availability(inventory, order, *maybe):
    inventory = deque(inventory)
    if order == "delivery":
        for current_delivery in maybe:
            inventory.append(current_delivery)

    elif order == "sell":
        if maybe:
            if type(maybe[0]) == int:
                for _ in range(maybe[0]):
                    inventory.popleft()
            else:
                for item in maybe:
                    if item in inventory:
                        while item in inventory:
                            inventory.remove(item)
        else:
            inventory.popleft()
    return list(inventory)