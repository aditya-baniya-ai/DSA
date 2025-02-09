import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap.
        # This heap will maintain the k largest elements encountered so far.
        minHeap = []
        
        # Iterate through each number in the list.
        for num in nums:
            # Push the current number onto the heap.
            heapq.heappush(minHeap, num)
            
            # If the heap size exceeds k, remove the smallest element.
            # This ensures that only the k largest elements remain in the heap.
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # After processing all elements, the smallest element in the heap
        # is the kth largest element in the array.
        return minHeap[0]
