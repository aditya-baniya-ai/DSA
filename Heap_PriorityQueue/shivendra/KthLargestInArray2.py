import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Transform the list 'nums' into a heap in-place.
        # Note: heapq implements a min-heap, so the smallest element is at index 0.
        heapq.heapify(nums)
        
        # Remove the smallest elements until the heap's size is exactly k.
        # After this loop, the heap will contain the k largest elements from the original list.
        while len(nums) > k:
            # Remove the smallest element from the heap.
            heapq.heappop(nums)
        
        # At this point, the heap contains exactly k elements.
        # The smallest element in this heap (nums[0]) is the kth largest element overall.
        return nums[0]
