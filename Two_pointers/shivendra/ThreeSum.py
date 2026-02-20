def threeSum(nums):
    nums.sort()  # Required for two-pointer technique and duplicate skipping
    res = []
    n = len(nums)

    # Iterate through each number as the fixed anchor
    for i, v in enumerate(nums):

        # Skip duplicate anchors to avoid repeated triplets
        if i > 0 and v == nums[i - 1]:
            continue

        # Initialize two pointers
        l, r = i + 1, n - 1

        # Two-pointer sweep for remaining two numbers
        while l < r:
            s = v + nums[l] + nums[r]

            if s < 0:
                # Need a larger sum → move left pointer right
                l += 1
            elif s > 0:
                # Need a smaller sum → move right pointer left
                r -= 1
            else:
                # Found a valid triplet
                res.append([v, nums[l], nums[r]])

                # Move both pointers to continue searching
                l += 1
                r -= 1

                # Skip duplicate values on the left pointer
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                # Skip duplicate values on the right pointer
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
#O(N^2), best approach humankind has known
# Time Complexity:
# Sorting takes O(n log n)
# Outer loop runs O(n)
# Inner two-pointer scan runs O(n)
# Total time complexity: O(n^2)

# Space Complexity:
# Output list can store up to O(n^2) triplets in worst case
# Ignoring output storage, extra space used is O(1)
# Total auxiliary space: O(1)
