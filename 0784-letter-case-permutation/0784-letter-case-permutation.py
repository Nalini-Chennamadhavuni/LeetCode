class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s.isdigit():
            return [s]
        elif len(s) == 1:
            return [s,s.lower()] if s.isupper() else [s,s.upper()]
       
        
       
        lu_sequence = ((c.lower(), c.upper()) for c in s)
        return list(set([''.join(x) for x in itertools.product(*lu_sequence)]))