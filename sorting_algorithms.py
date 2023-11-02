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


def inserion_sort(A:list, n:int):
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


def merge_sort(A, p, r):
    """
    Функция сортировки слиянием
    :param A: массив элементов размера
    :param p: начальный индекс массива
    :param r: конечный индекс массива
    :return: отсортированный в неубывающем порядке массив A
    """
    if p >= r - 1:
        return A
    else:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        return merge(A, p, q, r)


def merge(A:list, p:int, q:int, r:int):
    """
    Функция слияния
    :param A: массив данных
    :param p: минимальный индекс
    :param q: средний индекс
    :param r: максимальный индекс
    :return: отсортированный массив в пределах p и r
    """
    n = q - p + 1
    m = r - q
    B = A[p:q].copy()
    C = A[q:r].copy()
    B = np.append(B, 1000000)
    C = np.append(C, 1000000)
    i, j = 0, 0
    for k in range(p, r):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
    return A


if __name__ == "__main__":
    # print(binary_search.__doc__)
    # c = np.arange(0, 100000)
    # start = time.time()
    # find = sentinel_linear_search(c, len(c), 999)
    # print(time.time() - start)
    # start = time.time()
    # find = binary_search(c, len(c), 999)
    # print(time.time() - start)
    a = np.random.randint(1, 1000000, 10000)
    start = time.time()
    selection_sort(a, len(a))
    print("Сортировка выбором: ", time.time() - start)
    b = np.random.randint(1, 1000000, 10000)
    start = time.time()
    selection_sort_2(b, len(b))
    print("Сортировка выбором: ", time.time() - start)
    start = time.time()
    d = np.random.randint(1, 1000000, 10000)
    inserion_sort(d, len(d))
    print("Сортировка вставкой: ", time.time() - start)
    start = time.time()
    e = np.random.randint(1, 1000000, 1000)
    # print(merge_sort(e, 0, len(e)))
    print("Сортировка слиянием: ", time.time() - start)