from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert each stone weight to a negative value.
        # This is done because Python's heapq implements a min-heap by default,
        # and by negating the values, we effectively simulate a max-heap.
        stones = [-num for num in stones]
        
        # Transform the list into a heap in-place.
        heapq.heapify(stones)
        
        # Continue processing while there is more than one stone in the heap.
        while len(stones) > 1:
            # Pop the two largest stones (remember, they are stored as negatives).
            first = heapq.heappop(stones)  # Largest stone (as negative value)
            second = heapq.heappop(stones) # Second largest stone (as negative value)
            
            # If the two stones are not equal, push the difference back into the heap.
            # The difference is computed as first - second (both negatives).
            # For example, if first = -8 and second = -6, then first - second = -2,
            # which represents a stone with weight 2.
            if first != second:
                heapq.heappush(stones, first - second)
        
        # If no stones are left, the answer should be 0.
        # By appending 0, we ensure that stones[0] exists.
        stones.append(0)  # Adding 0 in case the heap is empty
        
        # Return the absolute value of the remaining stone (convert negative back to positive).
        return abs(stones[0])
