nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(nums)):
# #     current = nums[i]
pass

for i in range(len(nums)):
     current = nums[i]
     for j in range(i + 1):
         print(nums[j], end=' | ')
     print()