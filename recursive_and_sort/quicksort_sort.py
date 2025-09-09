def quicksort(arr):
    new_arr = arr.copy()
    if len(new_arr) <= 1:
        return new_arr
    pivot = new_arr[len(new_arr) // 2]
    left = [x for x in new_arr if x < pivot]
    middle = [x for x in new_arr if x == pivot]
    right = [x for x in new_arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(quicksort(numbers))
