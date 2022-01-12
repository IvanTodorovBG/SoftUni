

def data_types(type, command):

    if type == "int":
        integer_num = int(command)
        answer = integer_num * 2
        print(answer)
    elif type == "real":
        float_num = float(command)
        answer = float_num * 1.5
        print(f"{answer:.2f}")
    elif type == "string":
        print(f"${command}$")


data_types(input(), input())
