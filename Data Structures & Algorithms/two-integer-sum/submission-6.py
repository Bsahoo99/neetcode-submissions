class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            seen[nums[i]] = i

        for i in range(n):
            comp = target - nums[i]

            if comp in seen and seen[comp] != i:
                return [i,seen[comp]]        