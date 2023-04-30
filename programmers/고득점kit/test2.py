from itertools import permutations as pm
nums = [3,3,3,2,2,4]

for i in pm(nums, len(nums)//2):
    print(i)
