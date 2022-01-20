string = input().split(" ")

world_filter = list(filter(lambda x: len(x) % 2 == 0, string))

print("\n".join(world_filter))
