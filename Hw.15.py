def exit_quest(val):  # Check input value for exit.
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (val.lower()):
            return True
    return False


def check_isdigit(value):
    new_value = value
    check_minus = new_value.find('-')
    check_point = new_value.find('.')
    check_comma = new_value.find(',')
    if check_minus >= 0:
        new_value = new_value.replace('-', '', 1)
    if check_point >= 0 or check_comma >= 0:
        if check_point >= 0:
            new_value = new_value.replace('.', '', 1)
        elif check_comma >= 0:
            new_value = new_value.replace(',', '', 1)
    if new_value.isdigit():
        if value[:1] == '-':
            if check_point >= 0 or check_comma >= 0:
                if value[1:2] == '.' or value[1:2] == ',':
                    new_minus = f'''Ви ввели від'ємне дробове число: -0.{new_value}'''
                    return new_minus
                else:
                    new_minus = f'''Ви ввели від'ємне дробове число: {value}'''
                    return new_minus
            else:
                new_minint = f'''Ви ввели від'ємне число: {value}'''
                return new_minint
        else:
            if check_point >= 0 or check_comma >= 0:
                new_intdb = f'Ви ввели позитивне дробове число: {value}'
                return new_intdb
            else:
                new_int = f'Ви ввели позитивне ціле число: {value}'
                return new_int
    else:
        return False


while True:
    input_value = input('Number required: ')
    if exit_quest(input_value):
        break
    if not check_isdigit(input_value):
        print(f'Ви ввели неправильне число: {input_value}')
        pass
    else:
        print(check_isdigit(input_value))
        break
