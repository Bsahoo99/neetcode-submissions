class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countSet = set()

        for i in nums:
            if i not in countSet:
                countSet.add(i)
            else: 
                return True 
        return False            