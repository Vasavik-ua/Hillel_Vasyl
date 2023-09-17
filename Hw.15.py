def exit_quest(value):  # Check input value for exit.
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (value.lower()):
            return True
    return False


def check_isdigit(value):
    new_value = ()
    check_minus = value.find('-')
    check_point = value.find('.')
    check_comma = value.find(',')
    if check_minus >= 0:
        new_value = value.replace('-', '', 1)
    if check_point >= 0 or check_comma >= 0:
        if check_point >= 0:
            new_value = value.replace('.', '', 1)
        elif check_comma >= 0:
            new_value = value.replace(',', '', 1)
    if new_value.isdigit():
        return new_value
    else:
        print(f'Ви ввели неправильне число: {value}')
        return False



while True:
    input_value = input('Number required: ')
    if exit_quest(input_value):
        break
    if check_isdigit(input_value) == False:
        pass
    else:
        break


