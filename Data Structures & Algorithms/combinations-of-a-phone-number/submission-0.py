class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r = []
        p = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if digits == "":
            return []
        def b(i,s):
            if i == len(digits):
                r.append(s)
                return 
            
            for k in p[digits[i]]:
                ch = k
                b(i+1,s + ch)
        b(0,"")
        return r