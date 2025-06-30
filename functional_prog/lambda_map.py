print((lambda x, y: x + y)(5, 3))

nums = [1, 3, 2, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)


print("-------------------------")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))


print("-------------------------")


numbers = [1, 2, 3, 4, 5]
squared_numbers = [x * x for x in numbers]
print(squared_numbers)


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)
