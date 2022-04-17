n = int(input())
longest_intersection = []
for _ in range(n):

    first_info, second_info = input().split("-")
    first_start, first_end = [int(i) for i in first_info.split(",")]
    second_start, second_end = [int(i) for i in second_info.split(",")]

    first_list = [i for i in range(first_start, first_end + 1)]
    second_list = [i for i in range(second_start, second_end + 1)]

    intersection = set(first_list) & set(second_list)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
