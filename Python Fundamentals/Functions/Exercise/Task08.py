

def palindrome_integers(numbers):

    for current_number in numbers:
        if current_number == current_number[::-1]:
            print("True")
        else:
            print("False")


palindrome_integers(input().split(", "))
