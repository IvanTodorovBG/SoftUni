def total_sum(numbers):
    answer = []
    positive_numbers = sum([el for el in numbers if el >= 0])
    negative_numbers = sum([el for el in numbers if el < 0])
    answer.append(negative_numbers)
    answer.append(positive_numbers)
    if abs(positive_numbers) > abs(negative_numbers):
        answer.append("The positives are stronger than the negatives")
    elif abs(negative_numbers) > abs(positive_numbers):
        answer.append("The negatives are stronger than the positives")
    return "\n".join([str(el) for el in answer])


print(total_sum([int(el) for el in input().split()]))
