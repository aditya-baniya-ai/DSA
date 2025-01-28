
def containsDuplicate(nums):
        d={}
        for num in nums:
            if num in d:
                return True
            d[num]= 1
        return False
    
print(containsDuplicate([1,2,4,3,6,]))