class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsdict = {}
        for i,n in enumerate(nums):
            if target - n in numsdict:
                return [numsdict[target-n], i]
            else:
                numsdict[n] = i
           
           