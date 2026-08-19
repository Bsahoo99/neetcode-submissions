class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        N = len(nums)
        for n in range(N - 1):
            if nums[n] == nums[n + 1]:
                return True
        return False