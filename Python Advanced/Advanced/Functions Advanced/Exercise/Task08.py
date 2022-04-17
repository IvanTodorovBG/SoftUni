def age_assignment(*args, **kwargs):
    answer = {}
    for arg in args:
        for k, v in kwargs.items():
            if arg[0] == k:
                answer[arg] = v
    return answer


