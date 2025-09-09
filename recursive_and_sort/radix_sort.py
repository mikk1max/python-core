def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    # Оновлення count[i] так, щоб він показував позицію наступного входження своєї цифри
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radix_sort(arr):
    # Визначення максимального числа для визначення кількості розрядів
    new_arr = arr.copy()
    max_num = max(new_arr)
    position = 1
    # Виконання counting_sort для кожного розряду
    while max_num // position > 0:
        counting_sort(new_arr, position)
        position *= 10
    return new_arr

arr = [3, 89, 67, 254, 9, 21, 185, 4, 62]
print("Початковий масив:", arr)
print("Відсортований масив:", radix_sort(arr))
