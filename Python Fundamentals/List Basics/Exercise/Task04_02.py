beggars_jobs = [int(x) for x in input().split(", ")]
count_of_beggars = int(input())

final_list = []

for num in range(count_of_beggars):
    jobs = 0
    for index in range(num, len(beggars_jobs), count_of_beggars):
        jobs += beggars_jobs[index]
    final_list.append(jobs)

print(final_list)
