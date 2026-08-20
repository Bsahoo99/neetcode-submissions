class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevset = {}
        n = len(nums)

        for i in range(n):
            prevset[nums[i]] = i

        for i in range(n):
            diff = target - nums[i]

            if diff in prevset and prevset[diff] != i:
                return [i,prevset[diff]]