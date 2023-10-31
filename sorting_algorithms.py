import numpy as np
import time

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


def selection_sort(A:list, n:int):
    """
    Функция сортировки выбором
    :param A: массив элементов размера n
    :param n: размер массива
    :return: отсортированный по возрастанию массив A
    """
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]:
                # smallest = i
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A


def selection_sort_2(A: list, n: int):
        """
        Функция сортировки выбором
        :param A: массив элементов размера n
        :param n: размер массива
        :return: отсортированный по возрастанию массив A
        """
        for i in range(n - 1):
            smallest = i
            for j in range(i + 1, n):
                if A[j] < A[smallest]:
                    smallest = j
                    temp = A[i]
                    A[i] = A[smallest]
                    A[smallest] = temp
        return A


def inserion_sort(A, n):
    """
    Функция сортировки вставкой
    :param A: массив элементов размера n
    :param n: размер массива
    :return: отсортированный по возрастанию массив A
    """
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A



if __name__ == "__main__":
    print(binary_search.__doc__)
    a = np.random.randint(1, 1000, 1000)
    start = time.time()
    selection_sort(a, len(a))
    print(time.time() - start)
    b = np.random.randint(1, 1000, 1000)
    start = time.time()
    selection_sort_2(b, len(b))
    print(time.time() - start)
    c = np.arange(0, 100000)
    start = time.time()
    find = sentinel_linear_search(c, len(c), 999)
    print(time.time() - start, find)
    start = time.time()
    find = binary_search(c, len(c), 999)
    print(time.time() - start, find)
    d = np.random.randint(1, 100, 100)
    print(d)
    print(inserion_sort(d, len(d)))