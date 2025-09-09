def selection_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if new_arr[j] < new_arr[min_idx]:
                min_idx = j
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
    return new_arr

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(selection_sort(numbers))
