def next_greater_element(nums1, nums2):
    stack = []
    output_array = {}
    i = len(nums2)-1
    
    while i >= 0:
        while stack and nums2[i] >= stack[-1]:
            stack.pop()
            
        if not stack:
            output_array[nums2[i]] = -1
            
        else:
            output_array[nums2[i]] =stack[-1]
            
        stack.append(nums2[i])
        i-=1
        
    
    return [output_array[num] for num in nums1]
        
print(next_greater_element([4,1,2],[1,3,4,2]))
            
    