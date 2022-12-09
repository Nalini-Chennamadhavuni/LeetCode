class Solution(object):
#Dictionary 

    def twoSum(self, nums, target):
        numsdict={}
        for i,num in enumerate(nums):
            if target - num in numsdict:
                return numsdict[target - num], i
            else:
                numsdict[num] = i