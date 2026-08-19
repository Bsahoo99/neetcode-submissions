class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countset = set()

        for n in nums:
            if n in countset:
                return True 
            countset.add(n)
        return False        
