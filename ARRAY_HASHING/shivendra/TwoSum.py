def twoSum(nums, target):
    d={}
    for i, num in enumerate(nums):
        diff =  target - num
        if diff in d:
            return [d[diff],i] 
        else: 
            d[num] = i

print(twoSum([1,2,5,3,1],8))