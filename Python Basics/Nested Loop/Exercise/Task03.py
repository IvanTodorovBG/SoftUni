command = input()
prime_number = 0
non_prime_number = 0
while command != "stop":
    is_prime = True
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue
    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break
    if is_prime:
        prime_number += current_number
    else:
        non_prime_number += current_number
    command = input()
print(f"Sum of all prime numbers is: {prime_number}")
print(f"Sum of all non prime numbers is: {non_prime_number}")