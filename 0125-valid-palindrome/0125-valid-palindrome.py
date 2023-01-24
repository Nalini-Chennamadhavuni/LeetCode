class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        
        begin = 0
        end = len(s) -1
        if len(s) == 1:
            return True
        
        while begin < end:
            if s[begin].lower() != s[end].lower():
                return False   
            begin += 1
            end -=1
        return True