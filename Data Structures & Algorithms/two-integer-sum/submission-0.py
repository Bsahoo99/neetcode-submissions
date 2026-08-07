class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_to_index = {}

        for index, n in enumerate(nums):
            complement = target - n

            if complement in nums_to_index:
                return[nums_to_index[complement], index]

            nums_to_index[n] = index   