def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right: #Donot forget = after <
        mid = left + (right - left) // 2  # Calculate mid-point

        if nums[mid] == target:  # Target found
            return mid
        elif target > nums[mid]:  # Search right half
            left = mid + 1
        else:  # Search left half
            right = mid - 1

    return -1  # Target not found

print(binary_search([-1,0,3,5,9,12],9))