''' def singleNumber(nums):  #uses dict to store and check for the key
 whose value is 1 as the rest would have 2
        d={}
        for num in nums:
            d[num]= 1+ d.get(num,0)

        for key,value in d.items():
                if value==1:
                    return key '''
def singleNumber(nums): #uses xor, 111 rule: returns 1 if there is 1 1.
    xor=0
    for num in nums:
        xor^=num
    return xor

print(singleNumber([2,2,1]))
print(singleNumber([4, 1, 2, 1, 2]))