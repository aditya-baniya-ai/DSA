# o(n) key concept-> hashmap

def two_sum(nums, target):
    dictionary={}
    
    for index, num in enumerate(nums):
        diff = target - num
        
        if diff in dictionary:
            return [dictionary[diff], index]
        else:
            dictionary[num] = index
            
    return -1
            
            
print(two_sum([3,3], 6))
    