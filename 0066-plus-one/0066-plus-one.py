class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
                
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        if len(digits) == 1 and digits[-1] == 9:
            return [1,0]
        
        carry = 0
        for i in range(len(digits)-1,-1,-1):
           
            if digits[i] == 9 and i != 0:
                digits[i] = 0
                carry = 1
            
            elif digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0,1)
                
            elif carry and digits[i] < 9:
                digits[i] += carry 
                break
                
        return digits