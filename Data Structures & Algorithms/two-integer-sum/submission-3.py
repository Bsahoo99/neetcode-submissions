class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for n in range(len(nums)):
            x = target - nums[n]
            if x in nums:
                y = nums.index(x)
                if n != y:
                    ans = [min(n, y), max(n, y)]
                    break
        return ans