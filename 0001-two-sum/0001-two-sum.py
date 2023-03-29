class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #numdict = {}
        for i,n in enumerate(nums):
            print("n is", n)
            if target-n in nums and nums.index(target-n) != i:
                return [nums.index(target-n), i]
