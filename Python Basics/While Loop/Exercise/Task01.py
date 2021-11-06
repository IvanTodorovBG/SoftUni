searched_book = input()
books = input()
count = 0
while books != "No More Books":
    count += 1
    if books == searched_book:
        print(f"You checked {count-1} books and found it.")
        break
    books = input()
if books == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {count} books.")
