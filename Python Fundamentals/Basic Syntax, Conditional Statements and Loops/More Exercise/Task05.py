word = input()

search_word = ("Sand", "Water", "Fish", "Sun")

counter = 0
times_found = 0

for current_word in search_word:
    if current_word.lower() in word.lower():
        times_found = word.lower().count(current_word.lower())

        counter += times_found

print(counter)
