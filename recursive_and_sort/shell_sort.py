def shell_sort(arr):
    new_arr = arr.copy()
    n = len(new_arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = new_arr[i]
            j = i
            while j >= gap and new_arr[j - gap] > temp:
                new_arr[j] = new_arr[j - gap]
                j -= gap
            new_arr[j] = temp
        gap //= 2

    return new_arr

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(shell_sort(numbers))