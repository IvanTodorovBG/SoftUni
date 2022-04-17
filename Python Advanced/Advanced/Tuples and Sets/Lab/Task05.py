n = int(input())
vip_guest = set()
regular_guest = set()

for _ in range(n):

    reservation_code = input()

    if reservation_code[0].isdigit():
        vip_guest.add(reservation_code)
    else:
        regular_guest.add(reservation_code)

command = input()

while command != "END":

    if command[0].isdigit():
        vip_guest.discard(command)
    else:
        regular_guest.discard(command)

    command = input()

missing_guest = len(vip_guest) + len(regular_guest)

print(missing_guest)

for vip in sorted(vip_guest):
    print(vip)

for regular in sorted(regular_guest):
    print(regular)
