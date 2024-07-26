# Пузырьковая сортировка (Bubble Sort)
    # Пузырьковая сортировка сравнивает соседние элементы и меняет их местами, если они стоят в неправильном порядке.
    # Этот процесс повторяется до тех пор, пока массив не будет отсортирован.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если ни одного обмена не было, массив уже отсортирован
        if not swapped:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Отсортированный массив (Пузырьковая сортировка):", sorted_arr)

# Сортировка выбором (Selection Sort)
    # Сортировка выбором находит минимальный элемент из неотсортированной части массива и меняет его местами
    # с первым элементом этой части. Этот процесс повторяется для всех элементов массива.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Ищем минимальный элемент в неотсортированной части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем найденный минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Отсортированный массив (Сортировка выбором):", sorted_arr)

# Сортировка вставками (Insertion Sort)
    # Сортировка вставками строит отсортированный массив поэлементно. Каждый новый элемент вставляется в уже
    # отсортированную часть массива на нужное место.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы массива, которые больше текущего элемента, вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Отсортированный массив (Сортировка вставками):", sorted_arr)

# Быстрая сортировка (Quick Sort)
    # Быстрая сортировка выбирает опорный элемент и делит массив на две части: элементы меньше опорного и
    # элементы больше опорного. Этот процесс повторяется рекурсивно для каждой части.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Рекурсивно сортируем подмассивы и объединяем их с опорным элементом
        return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив (Быстрая сортировка):", sorted_arr)

# Сортировка слиянием (Merge Sort)
    # Сортировка слиянием делит массив на две части, рекурсивно сортирует каждую часть, а затем объединяет
    # отсортированные части в один массив.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Рекурсивно сортируем первую и вторую половины
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Объединяем отсортированные половины
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Отсортированный массив (Сортировка слиянием):", sorted_arr)
