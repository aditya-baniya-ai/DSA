from typing import List


def productExceptSelf(nums):
    # Get the length of the input array.
    n = len(nums)
    
    # 'prefix' will hold the cumulative product of all elements to the left of the current index.
    prefix = 1
    # 'postfix' will hold the cumulative product of all elements to the right of the current index.
    postfix = 1
    
    # Initialize the result array with 1's.
    # Each position in 'res' will eventually contain the product of all numbers
    # in the array except the number at that position.
    res = [1] * n
    
    # First pass: Calculate the prefix product for each index.
    # For index i, store the product of all numbers to its left.
    for i in range(n):
        res[i] = prefix    # Set the current result to the prefix product.
        prefix *= nums[i]  # Update prefix to include the current element.
    
    # Second pass: Calculate the postfix product and update the result.
    # Iterate from right to left.
    for i in range(n - 1, -1, -1):
        res[i] *= postfix  # Multiply the current result with the postfix product.
        postfix *= nums[i] # Update postfix to include the current element.
    
    # The 'res' list now contains the product of all elements except self at each index.
    return res


print(productExceptSelf([1,2,3,4])) #O/P: [24, 12, 8, 6]