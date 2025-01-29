def threeSum(nums): #twosum method with binary search and two pointers
    nums.sort()
    res =[]
    n=len(nums)

    for i, v in enumerate(nums): #index,value
        #checking 2nd element with 1st to avoid duplicate checks with pointers
        if i>0 and v==nums[i-1]: 
            continue

        l,r= i+1, n-1 #l starts on right of v

        while l<r:
            threesum= v+nums[l]+nums[r]

            if threesum<0:
                l+=1
            elif threesum>0:
                r-=1

            else: #threeSum found and add to the list
                res.append([v,nums[l],nums[r]])
                l+=1 # regular pointer slide
                while nums[l]==nums[l-1] and l<r: #avoiding duplicate checks for l with r
                    l+=1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
#O(N^2), best approach humankind has known