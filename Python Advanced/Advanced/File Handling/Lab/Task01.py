try:
    file = open("aaa.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")

