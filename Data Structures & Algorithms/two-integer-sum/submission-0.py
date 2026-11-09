class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for index, num in enumerate(nums):
            complement = target-num
            if complement not in seen:
                seen[num] = index
            else:
                return [seen[complement], index]
            
             