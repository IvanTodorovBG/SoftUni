def sorting_cheeses(**cheeses):
    result = []
    sorted_cheeses = dict(sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in sorted_cheeses.items():
        result.append(key)
        for num in sorted(value, reverse=True):
            result.append(num)
    return '\n'.join([str(el) for el in result])

