""" 
    first we calculate the sum
    then check if sum is greater than k or not.
    if it is then we remove elements from left and shrink the window
    else we keep adding from right until we have sum less than or equal to k
"""

def longest_subarray(nums,k):
    l=r=0
    max_len = 0
    max_sum=0
    
    while r<len(nums):
        max_sum = max_sum+ nums[r]
        
        if(max_sum >k):
            max_sum = max_sum - nums[l]
            l+=1
            
        if (max_sum<=k):
            max_len= max(max_len, r-l+1)
            
        r+=1
        
    return max_len
    
print(longest_subarray([2,5,1,7,10],14))