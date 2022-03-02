text = input().split("\\")
new_text = text[-1].split(".")

print(f"File name: {new_text[0]}")
print(f"File extension: {new_text[1]}")
