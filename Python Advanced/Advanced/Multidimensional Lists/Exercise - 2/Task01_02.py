matrix = [sublist.split() for sublist in input().split("|")][::-1]
print(' '.join([str(number) for sublist in matrix for number in sublist]))


