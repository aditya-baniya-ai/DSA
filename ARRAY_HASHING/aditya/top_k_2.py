from collections import Counter

# what did i do? = first i counted how many the numbers are repeated and made a key:value pair(i could do this also using defaultdict(int))
# dic = defaultdict(int)
# for i in nums):
#   dic[i]+=1
#
# After that i sorted the dictionary using built-in sorted function with the help of lambda function with reverse=True(the maximum will be in top)
#
# How lambda works? = we are sorting dic.items() with key = the value of dic. x[1] denotes the values
#
# sorted(item to sort, key on which to sort, reverse)
#
# Then i need to find k elements from top(or k max elements) then i will append the top k elements to final and return final

# logic: count, sort, append the top k elements and return   (its that easy)

def topKFrequent(nums, k):
    dic = Counter(nums)
    
    final=[]
    count=0
    sorted_dic = sorted(dic.items(), key= lambda x:x[1], reverse=True)
    
    for i in range(k):
        final.append(sorted_dic[count][0])
        count+=1
        
    return final
    
print(topKFrequent([1,1,1,2,2,3],2))
    