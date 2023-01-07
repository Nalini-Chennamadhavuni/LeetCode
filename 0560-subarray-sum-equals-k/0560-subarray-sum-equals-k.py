class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0 
        res = 0
        prefixSum = {0:1}
        
        for n in nums:
            currSum += n
            diff = currSum - k 
            res += prefixSum.get(diff,0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum,0)
            
        return res