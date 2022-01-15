def no_vowels(words):
    vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
    no_vowels_list = "".join([x for x in words if x not in vowels])
    return no_vowels_list


print(no_vowels(input()))

