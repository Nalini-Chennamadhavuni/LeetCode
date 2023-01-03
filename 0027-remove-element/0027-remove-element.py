class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        stack = []
        for i in range(len(nums)):
            if nums[i] != val:
                stack.append(nums[i])
                nums[len(stack)-1] = nums[i]
        return len(stack)