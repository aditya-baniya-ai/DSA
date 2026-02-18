def twoSumTwo(nums, target):
    l, r = 0, len(nums)-1

    while l<r:
        summ = nums[l] + nums[r]
        if target > summ: l += 1
        elif target < summ: r -= 1
        elif target == summ: return [l+1, r+1]
    return -1

print(twoSumTwo([2,7,11,15],9))
