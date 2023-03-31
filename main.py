##########################
#Цыбикжапов Даши БПМ-21-1#
##########################

#Рассмотрим реализацию сортировки Timsort на Python
# для сортировки массива чисел по возрастанию.

#Сортировка Timsort - это гибридный алгоритм сортировки,
# который объединяет в себе сортировку вставками и сортировку слиянием.

def timsort(arr):
    # Задаем размер минимальной подсекции, которая будет сортироваться вставками
    min_run = 32

    # Разбиваем массив на подсекции
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    # Сливаем подсекции, пока не получим отсортированный массив
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n, start + size)
            end = min(n, start + size * 2)
            merged_array = merge(arr[start:mid], arr[mid:end])
            arr[start:end] = merged_array
        size *= 2
    return arr


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


# Пример использования
arr = [3, 5, 2, 6, 8, 12, 0, 4, 9, 7]
sorted_arr = timsort(arr)
print(sorted_arr)

#В этом примере мы сначала разбиваем массив на подсекции, каждая из которых сортируется с помощью сортировки вставками.
#Затем мы сливаем подсекции, пока не получим отсортированный массив.
#Функция insertion_sort выполняет сортировку вставками,
#а функция merge выполняет слияние двух отсортированных подмассивов.
#Функция timsort использует эти функции для сортировки массива arr.
#Результатом работы данного кода будет отсортированный
#массив sorted_arr, который будет содержать [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]