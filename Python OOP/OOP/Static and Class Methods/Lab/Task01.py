class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for current_num in args:
            result *= current_num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for current_num in args[1:]:
            result /= current_num
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for current_num in args[1:]:
            result -= current_num
        return result
