def bubble_sort(lst):
    arr = lst.copy()
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(bubble_sort(numbers))