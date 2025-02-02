def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    # Traverse nums2 in reverse order to populate next_greater map
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)

    # Use list comprehension for efficient lookup
    return [next_greater[num] for num in nums1]


print(nextGreaterElement([4,1,2],[1,3,4,2]))