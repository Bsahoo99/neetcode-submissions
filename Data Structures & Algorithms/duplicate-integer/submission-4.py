class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        l,r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l += 1
            r += 1
        return False        