def insertion_sort(lst):
    arr = lst.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(insertion_sort(numbers))

