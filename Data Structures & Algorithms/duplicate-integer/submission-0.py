class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:
            seen[number] = seen.get(number, 0) + 1
        for count in seen.values():
            if count > 1:
                return True
        return False
            

        