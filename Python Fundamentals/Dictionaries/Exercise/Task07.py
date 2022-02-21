number_of_commands = int(input())
parking_register = {}

for current_command in range(number_of_commands):

    command = input().split()

    # register or unregister command:
    order = command[0]

    # key dictionary
    username = command[1]

    #registering the cars
    if order == "register":
        # value dictionary
        license_plate_number = command[2]

        if username in parking_register:
            print(f"ERROR: already registered with plate number {parking_register[username]}")
        else:
            parking_register[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    #unregistering the cars
    elif order == "unregister":

        if username not in parking_register:
            print(f"ERROR: user {username} not found")
        else:
            parking_register.pop(username)
            print(f"{username} unregistered successfully")

print("\n".join(f"{k} => {v}" for k, v in parking_register.items()))
