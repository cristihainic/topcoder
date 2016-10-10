class SimpleCalculator:

    def calculate(self, input):

        first_num = ''
        second_num = ''
        operator = ''

        for i in input:
            if i.isdigit():
                first_num += i
            if not i.isdigit():
                operator = i

        for i in reversed(input):
            if i.isdigit():
                second_num += i
            if not i.isdigit():
                break

        second_num = second_num[::-1]

        if operator == '+':
            result = int(first_num) + int(second_num)
        elif operator == '-':
            result = int(first_num) - int(second_num)
        elif operator == '*':
            result = int(first_num) * int(second_num)
        else:
            result = int(first_num) / int(second_num)

        return result
