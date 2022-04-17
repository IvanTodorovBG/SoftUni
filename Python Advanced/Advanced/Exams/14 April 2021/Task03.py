def flights(*info):
    info = list(info)
    cities = info[::2]
    people = info[1::2]
    answer = {}
    for index, city in enumerate(cities):
        if city == "Finish":
            break
        if city not in answer:
            answer[city] = 0
        answer[city] += people[index]
    return answer



