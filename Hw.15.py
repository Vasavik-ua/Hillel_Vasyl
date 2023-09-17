def exit_quest(value):  # Check input value for exit.
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (value.lower()):
            return True
    return False


def check_isdigit(value):
    check_minus = value.find('-')
    if check_minus > 0:
        value.replace('-', '', 1)
    check_point = value.find('.')
    check_comma = value.find(',')
    if check_point > 0 or check_comma > 0:
        if check_point > 0:
            value.replace('.', '', 1)
        elif check_comma > 0:
            value.replace(',', '', 1)
    if value.isdigit():
        return True
    else:
        print(f'Ви ввели неправильне число: {value}')
        return False






while True:
    input_value = input('Number required: ')
    if exit_quest(input_value):
        break

