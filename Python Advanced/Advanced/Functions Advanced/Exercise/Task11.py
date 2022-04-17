from collections import deque


def math_operations(*nums, **dict):
    nums = deque(nums)
    list_of_tuples = deque(list([list(kvp) for kvp in dict.items()]))
    answer = {}
    while nums:
        current_num = nums.popleft()

        if list_of_tuples[0][0] == 'a':
            list_of_tuples[0][1] += current_num

        elif list_of_tuples[0][0] == 's':
            list_of_tuples[0][1] -= current_num

        elif list_of_tuples[0][0] == 'd':
            if current_num == 0:
                list_of_tuples.append(list_of_tuples.popleft())
                continue
            list_of_tuples[0][1] /= current_num

        elif list_of_tuples[0][0] == 'm':
            list_of_tuples[0][1] *= current_num

        list_of_tuples.append(list_of_tuples.popleft())

    for k, v in dict.items():
        for index in list_of_tuples:
            if index[0] == k:
                answer[k] = index[1]

    return answer




print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))