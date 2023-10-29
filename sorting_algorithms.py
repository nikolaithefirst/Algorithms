import numpy as np


def linear_sort(A:list, n:int):
    """
    Функция линейного поиска позиции элемента n в массиве A
    :param A: массив элементов размера k
    :param n: искомое значение
    :return: A(k) = n, если k есть в A или "Not found", если n не в A
    """

    for i in range(len(A)):
        if A[i] == n:
            return i
    return "Not found"


def sentinel_linear_search(A:list, n:int, x:int):
    """
    Функция линейного поиска позиции элемента n в массиве A
    :param A: массив элементов размера n
    :param n: размер массива
    :param x: искомое значение
    :return: позиция i, если A(i) = x, иначе "Not found"
    """
    last = A[n-1]
    A[n-1] = x
    i = 0
    while A[i] != x:
        i += 1
    if i < (n - 1) or last == n-1:
        return i
    return "Not found"


def binary_search(A:list, n:int, x:int):
    """
    Функция бинарного поиска позиции x в отсортированном массиве A
    :param A: отсортированный массив элементов размера n
    :param n: размер массива
    :param x: искомое значение
    :return: позиция i, если A(i) = x, иначе "Not found"
    """
    p, r = 0, n - 1
    while p <= r:
        q = (p + r) // 2
        if A[q] == x:
            return q
        elif A[q] > x:
            r = q - 1
        elif A[q] <= x:
            p = q + 1
    return "Not found"


if __name__ == "__main__":
    print(binary_search.__doc__)
