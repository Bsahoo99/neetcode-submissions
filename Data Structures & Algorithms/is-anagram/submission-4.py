class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsets = {}
        countsett = {}
        if len(s) == len(t):   

            for n in range(len(s)):
                countsets[s[n]] = 1 + countsets.get(s[n],0)

            for n in range(len(t)):
                countsett[t[n]] = 1 + countsett.get(t[n],0)

            if countsets == countsett:
                return True
            else:
                return False    
        else:
            return False        
