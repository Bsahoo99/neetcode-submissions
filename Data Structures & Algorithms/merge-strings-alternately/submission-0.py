class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        I, J = len(word1),len(word2)
        i,j = 0,0
        res = []

        while i < I and j < J:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)