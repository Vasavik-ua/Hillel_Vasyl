def exit_quest(value):
    check_list = ["вихід", "exit", "quit", "e", "q"]
    for item in range(len(check_list)):
        if check_list[item] == (value.lower()):
            return True
        else:
            pass
    return False

a = 'e'
b = exit_quest(a)
print(b)