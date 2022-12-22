class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        stack = []
        while i < len(nums):
            if not stack:
                stack.append(nums[i])
                
            else:
                if not nums[i] == stack[-1]:
                    stack.append(nums[i])
                    nums[len(stack)-1] = nums[i]
            i += 1
        
        return len(stack)