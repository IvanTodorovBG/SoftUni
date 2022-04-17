from collections import deque
customers = [int(num) for num in input().split(", ")]
taxis = [int(num) for num in input().split(", ")]
total_time = 0
customers_queue = deque(customers)

while True:

    if customers_queue and taxis:

        if taxis[-1] >= customers_queue[0]:
            total_time += customers_queue[0]
            customers_queue.popleft()
            taxis.pop()
        else:
            taxis.pop()

    else:
        break

if not customers_queue:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(num) for num in customers_queue])}")

