def productExceptSelf(nums):
        n= len(nums)
        res =[]
        for i in range(n):
            product =1 #initializing prouct for every num
            for j in range(n):
                if i!=j:
                    product *= nums[j]
            res.append(product)
        
        return res

print(productExceptSelf([1,2,3,4]))