class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        sortedList = sorted(d, key=d.get, reverse=True)
        return sortedList[:k]

# Time: O(n log n), not optimal but easy and intuitive
# Space: O(n), works for interviews