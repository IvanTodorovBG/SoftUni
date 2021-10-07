v = int(input())   # pool`s litters
p1 = int(input())   # litters per hour
p2 = int(input())
n = float(input())    # hours

litters_p1 = p1 * n
litters_p2 = p2 * n
all_litters_from_p1_p2 = litters_p1 + litters_p2
percent_pool = all_litters_from_p1_p2 / v * 100
percent_p1 = litters_p1 / all_litters_from_p1_p2 * 100
percent_p2 = litters_p2 / all_litters_from_p1_p2 * 100
overflow_pool = all_litters_from_p1_p2 - v # препълнен

if v >= all_litters_from_p1_p2:
    print(f"The pool is {percent_pool:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
elif v < all_litters_from_p1_p2:
    print(f"For {n:.2f} hours the pool overflows with {overflow_pool:.2f} liters.")