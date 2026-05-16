
def topKFrequent(nums, k):
    d = {}
    for num in nums:
        d[num] = 1 + d.get(num, 0)
    sorted_key = sorted(d, key=d.get, reverse=True)
# or sorted_key = sorted_key[::-1]
    return sorted_key[:k] #returns 0,1 indices if k = 2

# Time: O(n log n), not optimal but easy and intuitive
# Space: O(n), works for interviews

        