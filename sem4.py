"""
Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
"""

"""
def print_words_sorted(text):
    words = sorted(text.split(), key=lambda x: x.lower())
    max_word_len = max(len(word) for word in words)
    for i, word in enumerate(words, 1):
        spaces = " " * (max_word_len - len(word) + 1)
        print("{0}{1}{2}".format(i, spaces, word))


print_words_sorted(input("Введите текст: "))
"""
"""
Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

"""
def unique_unicode(text):
    unique_codes = list(set(ord(char) for char in text))
    return sorted(unique_codes, reverse=True)


print(unique_unicode(input("Введите текст: ")))
"""
"""
Функция получает на вход строку из двух чисел через пробел. Cформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число. Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

"""
def create_dict(s):
    x, y = map(int, s.split())
    min_val, max_val = min(x, y), max(x, y)
    result = {chr(i): i for i in range(min_val, max_val+1)}
    return result


print(create_dict(input("Введите два числа через пробел: ")))
"""
"""
Функция получает на вход список чисел. Отсортируйте его элементы in place без использования
встроенных в язык сортировок. Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""

"""
def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
    return nums


input_str = input("Введите числа, разделенные пробелом: ")
num_list = [int(num) for num in input_str.split()]
print(bubble_sort(num_list))
"""
"""
Функция принимает на вход три списка одинаковой длины:
- имена str,
- ставка int,
- премия str с указанием процентов вида «10.25%».
- Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
- Сумма рассчитывается как ставка умноженная на процент премии.
"""

"""
def calculate_bonus(names, rate, bonus):
    result = {}
    for i in range(len(names)):
        bonus_value = float(bonus[i][:-1]) / 100 * rate[i]
        result[names[i]] = bonus_value
    return result


names = ["Вася", "Петя", "Катя"]
rate = [100, 200, 300]
bonus = ["10.5%", "20%", "5%"]

result = calculate_bonus(names, rate, bonus)
print(result)
"""
"""
Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""

"""
def sum_between_indexes(numbers, index1, index2):
    start_index = min(index1, index2)
    end_index = max(index1, index2)
    if start_index < 0:
        start_index = 0
    if end_index > len(numbers) - 1:
        end_index = len(numbers) - 1
    return sum(numbers[start_index:end_index+1])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index1 = 2
index2 = 7
result = sum_between_indexes(numbers, index1, index2)
print(result)
"""

"""
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

"""
def calculate_profit_or_loss(companies):
    for company, finances in companies.items():
        total = sum(finances)
        if total < 0:
            return False
    return True

company_finances = {
    "Компания A": [100, 50, 25, -75],
    "Компания B": [10, 20, 30, 40],
    "Компания C": [200, 50, -100, 75, 25]
}

print(calculate_profit_or_loss(company_finances))
"""

"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

variable1 = 5
variable2s = "Hello"
variabl3 = [1, 2, 3]
variable4s = {"key": "value"}
variable5 = True


def replace_variables(variables):
    new_variables = []
    for variable in variables:
        if isinstance(variable, str) and variable.endswith('s') and len(variable) > 1:
            new_variables.append(None)
            new_variables.append(variable[:-1])
        else:
            new_variables.append(variable)
    return new_variables


variables = [variable1, variable2s, variabl3, variable4s, variable5]
new_variables = replace_variables(variables)
print(new_variables)