

def multiplication_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif num1 < 0 and num2 < 0 and num3 < 0:
        return "negative"
    elif num1 < 0 and num2 >= 1 and num3 >= 1:
        return "negative"
    elif num1 >= 1 and num2 < 0 and num3 >= 1:
        return "negative"
    elif num1 >= 1 and num2 >= 1 and num3 < 0:
        return "negative"
    else:
        return "positive"


print(multiplication_sign(int(input()), int(input()), int(input())))
