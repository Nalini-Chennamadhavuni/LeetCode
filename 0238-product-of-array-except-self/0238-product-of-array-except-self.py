class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        prodexceptself = [1] * len(nums) 
    
        for i in range(len(nums)):
            prodexceptself[i] = prefix 
            prefix  *= nums[i]
       
        suffix = 1
        for j in range(len(nums)-1,-1,-1):
            prodexceptself[j] *= suffix 
            suffix *= nums[j]
            
        return prodexceptself
            