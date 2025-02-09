import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build a frequency dictionary where the key is the number
        # and the value is the count of occurrences in the list 'nums'.
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)  # Increment count for each number

        # Step 2: Use a min-heap (priority queue) to keep track of the top k frequent numbers.
        # The heap will store tuples of the form (frequency, number).
        # By default, heapq in Python implements a min-heap, so the smallest frequency is at the root.
        heap = []
        for num in count.keys():
            # Push the tuple (frequency, number) into the heap.
            heapq.heappush(heap, (count[num], num))
            # If the heap size exceeds k, remove the smallest element (least frequent).
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract the k most frequent numbers from the heap.
        # Since we only need the number (and not its frequency), we extract the element at index [1]
        # from each tuple popped from the heap.
        ans = []
        for i in range(k):
            # heapq.heappop(heap) returns a tuple (frequency, num). Using [1] extracts the number.
            ans.append(heapq.heappop(heap)[1])
        
        # Return the list of top k frequent numbers.
        return ans
