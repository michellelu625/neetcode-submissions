class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        sorted_seen = sorted(seen, key=lambda x: seen[x], reverse=True)
        return sorted_seen[:k]