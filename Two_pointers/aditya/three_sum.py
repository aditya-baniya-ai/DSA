# fix one element and then the problem is two sum
# sort the list first and one pointer at first and one pointer at last
# if the sum > 0 , decrease the right pointer 
# if the sum < 0, increase the left pointer 
# use a set to remove any duplicates

def threeSum(nums):
    final_answer = set()
    nums = sorted(nums)
    
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        
        while left < right:
            sum_of_nums = nums[i] + nums[left]+nums[right]
            
            if sum_of_nums > 0:
                right-=1
            
            elif sum_of_nums < 0:
                left+=1
                
            else:
                final_answer.add((nums[i], nums[left], nums[right]))
                left+=1
                
    return list(final_answer)

print(threeSum([-1,0,1,2,-1,-4]))