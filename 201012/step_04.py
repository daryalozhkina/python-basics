nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# memory complexity
print(id(nums), nums)
nums.reverse()
print(id(nums), nums)
nums_2 = list(reversed(nums))
print(id(nums_2), nums_2) # memory complexity O(n)
# memory leaks
