from itertools import combinations as cb
nums = [3,3,3,2,2,4]

for i in cb(nums, len(nums)//2):
    print(i)
