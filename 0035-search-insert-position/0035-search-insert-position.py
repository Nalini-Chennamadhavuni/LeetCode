class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            for i,n in enumerate(nums):
                if n >= target:
                    return i
            return len(nums)