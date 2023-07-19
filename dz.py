from datetime import datetime

# Напишите функцию для транспонирования матрицы
print("--------------------------")
print("dz1")
print("--------------------------")
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0 for row in range(rows)] for col in range(cols)]

    for row in range(rows):
        for col in range(cols):
            transposed_matrix[col][row] = matrix[row][col]

    return transposed_matrix


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposed_matrix = transpose_matrix(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)

"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""

print("--------------------------")
print("dz2")
print("--------------------------")


def key_values(**kwargs):
    return {value: key for key, value in kwargs.items()}


my_dict = key_values(arg1='value1', arg2='value2')
print(my_dict)

"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно 
сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат.
- Начальная сумма равна нулю
- Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией
- Любое действие выводит сумму денег
"""
print("--------------------------")
print("dz3")
print("--------------------------")

context = {'summa': 0,
           'number_operations': 0,
           'percent': 0.015,
           'percent_10': 10,
           'max_fee': 600,
           'min_fee': 30,
           'message_three_operations': 'Начислены 3% от баланса за 3-и проведенных операции',
           'message_wealth_tax': 'Вычтен налог на богатство 10%',
           'replenishment_error': 'Ошибка пополнения: сумма должна быть кратна 50 у.е.',
           'withdrawal_error': 'Ошибка вывода: сумма должна быть кратна 50 у.е.',
           'input_error': 'Ошибка списания: вы ввели не число!',
           'insufficient_funds': 'Ошибка списания: на балансе недостаточно средств'}

operations = []

now = datetime.now()


def balance_top_up(context):
    if context['summa'] > 5000000:
        wealth_tax(context)
        return f"{context['message_wealth_tax']}, баланс: {context['summa']}."
    try:
        replenishment_amount = int(input("Внесите сумму: "))
        if replenishment_amount % 50 == 0:
            context['summa'] += replenishment_amount
            context['number_operations'] += 1
            operations.append(f"пополнение: {replenishment_amount} время: {now}")
            if context['number_operations'] == 3:
                modify_balance(context)
                return f"{context['message_three_operations']}. Баланс пополнен, на счете: {context['summa']}"
            return f"Баланс пополнен на {replenishment_amount}, сумма: {context['summa']}"
        else:
            return f"{context['replenishment_error']} Баланс: {context['summa']}"
    except ValueError:
        return f"{context['input_error']} Баланс: {context['summa']}"


def cash_withdrawal(context):
    if context['summa'] > 5000000:
        wealth_tax(context)
        return f"{context['message_wealth_tax']}, баланс: {context['summa']}."
    try:
        withdrawal_amount = int(input("Сумма снятия: "))
        percentages = max(min(withdrawal_amount * context['percent'], context['max_fee']), context['min_fee'])
        if withdrawal_amount % 50 == 0:
            if withdrawal_amount + percentages < context['summa']:
                context['summa'] -= percentages + withdrawal_amount
                context['number_operations'] += 1
                operations.append(f"списание: {withdrawal_amount} время: {now}")
                if context['number_operations'] == 3:
                    modify_balance(context)
                    return f"{context['message_three_operations']}. Сумма {withdrawal_amount} списана, на счете: {context['summa']}"
                return f"Снятие наличных выполнено. Баланс: {context['summa']} y.e."
            else:
                return f"{context['insufficient_funds']} Баланс: {context['summa']}"
        else:
            return f"{context['withdrawal_error']} Баланс: {context['summa']}"
    except ValueError:
        return f"{context['input_error']} Баланс: {context['summa']}"


def modify_balance(context):
    context['summa'] *= 0.97
    context['number_operations'] = 0


def wealth_tax(context):
    context['summa'] -= context['summa'] * context['percent_10'] / 100
    operations.append(f"налог на богатство: {context['summa']}, время: {now}")


def operation_historyions():
    for i in operations:
        print(i)


while True:
    num = input("Выберете действие (пополнить - 1, снять - 2, операции - 3, выход - 4): ")
    if num == '1':
        print(balance_top_up(context))
    elif num == '2':
        print(cash_withdrawal(context))
    elif num == '3':
        print("----------------------------------------")
        print("История операций:")
        print("----------------------------------------")
        operation_historyions()
        print("----------------------------------------")
    elif num == '4':
        print(f"Баланс: {context['summa']}, Работа с банкоматом завершена")
        break

