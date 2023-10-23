def linear_sort(A:list, n:int):
    """
    Функция линейного поиска позиции элемента n в массиве A
    :param A: массив элементов размера k
    :param n: искомый элемент
    :return: A(k) = n, если k есть в A или "Not found", если n не в A
    """

    for i in range(len(A)):
        if A[i] == n:
            return i
    return "Not found"


def sentinel_linear_search(A:list, n:int, x:int):
    """
    Функция линейного поиска позиции элемента n в массиве A
    :param A: массив элементов размера k
    :param n: размер массива
    :param x: искомый элемент
    :return: A(k) = n, если k есть в A или "Not found", если n не в A
    """
    last = A[n-1]
    A[n-1] = x
    i = 0
    while A[i] != x:
        i += 1
    if i < (n - 1) or last == n-1:
        return i
    return "Not found"
