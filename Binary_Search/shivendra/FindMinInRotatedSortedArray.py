def findMin(nums):
    l,r= 0, len(nums)-1 

    #l<r NOT l<=r
    while l<r: #exits and returns when l==r

        m = (l+r) // 2 #check midpoint
                
        if nums[m] > nums[r]: #if m>r, min is in right side
                    l = m + 1

        else: #else min is in left side, don't m-1 as m could be the min
            r = m

    return nums[l]
        
print(findMin([3,4,5,1,2]))