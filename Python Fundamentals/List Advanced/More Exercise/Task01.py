population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

sum_population = sum(population)
enough_wealth = min_wealth * len(population)
no_equal = False

if enough_wealth <= sum_population:
    for index, people in enumerate(population):
        wealthiest_person = max(population)
        wealthiest_person_index = population.index(wealthiest_person)
        for money in range(1, min_wealth + 1):
            if population[index] < min_wealth:
                population[index] += 1
                population[wealthiest_person_index] -= 1
else:
    no_equal = True

if no_equal:
    print("No equal distribution possible")
else:
    print(population)
