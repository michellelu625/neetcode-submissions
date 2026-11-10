class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement not in seen:
                seen[value] = index
            else:
                return [seen[complement], index]




            
             