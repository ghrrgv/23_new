#у исполнителя есть две команды
# - прибавить 1
# - умножить на 2
# определите количество программ исполнителя, которые преобразуют 1 в 14
# в ответ запишите число - кол-во программ
def task23(start, end):
    if start > end: return 0  # если стартовое число больше конечного, то решение не подходит
    if start == end: return 1  # если стартовое число = конечному, решение подходит
    if start < end: return task23(start+1, end) + task23(start*2, end)
# вызываем функцию обеих команд, в итоге task23 будет проверять уже изменённое начальное число если непонятно ты тупая
print(task23(1, 14))