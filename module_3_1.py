# Счётчик вызовов
calls = 0
def count_calls(): # считает вызовы остальных функций
    global calls
    calls += 1
    print(calls)
def string_info(string ): # принимает аргумент - строку и возвращает кортеж
    count_calls()
    string
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search): # принимает два аргумента: строку и список, и возвращает
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)