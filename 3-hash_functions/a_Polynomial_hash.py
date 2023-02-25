"""
A. Полиномиальный хеш

Алле очень понравился алгоритм вычисления полиномиального хеша.
Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений
отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:


Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание,
по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 106),
состоящая из больших и маленьких латинских букв.

Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.

Пример 1
Ввод	Вывод
123
100003
a
97
"""


def hash_from_c(a, m, string):
    tmp = ord(string[-1])
    length = a
    for c in string[-2::-1]:
        tmp = (tmp + ord(c) * length)
        length = (length * a) % m
    return tmp % m


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    if s == '':
        print(0)
    else:
        print(hash_from_c(a, m, s))