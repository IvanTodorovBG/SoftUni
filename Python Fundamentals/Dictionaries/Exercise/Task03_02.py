countrys = input().split(", ")
cities = input().split(", ")

new_dict = dict(zip(countrys, cities))

print("\n".join(f"{k} -> {v}" for k, v in new_dict.items()))
