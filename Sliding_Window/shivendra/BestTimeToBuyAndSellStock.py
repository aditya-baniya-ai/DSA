# uses sliding window as l slides with r
def maxProfit(nums):
    l=0
    maxp=0

    for r in range(1,len(nums)):
        if nums[r]>nums[l]:
            profit = nums[r]-nums[l]
            maxp= max(maxp,profit)
        else:
            l=r
    
    return maxp

print(maxProfit([7,1,5,3,6,4]))