def singleNumber(nums):
        d={}
        for num in nums:
            d[num]= 1+ d.get(num,0)

        for key,value in d.items():
                if value==1:
                    return key
print(singleNumber([2,2,1]))