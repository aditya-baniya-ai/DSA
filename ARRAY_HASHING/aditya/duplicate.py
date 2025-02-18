def find_deplicate(nums):
    
    dictionary = dict()
    
    for i in nums:
        if i in dictionary:
            return True
        
        else:
            dictionary[i] = 1
            
    return False
            
print(find_deplicate([1,2,2,3,4]))