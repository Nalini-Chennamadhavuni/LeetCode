class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        
        prodexceptself = [1] * len(nums) 
    
        for i in range(len(nums)):
            prodexceptself[i] = prefix 
            prefix  *= nums[i]
       
        
        for j in range(len(nums)-1,-1,-1):
            prodexceptself[j] *= suffix 
            suffix *= nums[j]
            
        return prodexceptself