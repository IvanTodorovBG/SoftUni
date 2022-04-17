from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

intelligence = int(input())
used_bullets = 0

while locks and bullets:
    bullet = bullets.pop()
    lock = locks[0]

    used_bullets += 1

    if lock >= bullet:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    if used_bullets % barrel_size == 0 and bullets:
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - used_bullets * bullet_price}")