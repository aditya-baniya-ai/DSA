#Bucket Sort
#Logic: make a hashmap and populate it, then make a bucket(list) of lists
#and populate it such as the the index of the list is the frequency and the value is value

def topKArray(nums,k):
    freq_map ={}
    freq = [[] for i in range(len(nums)+1)]

    #populate hashmap
    for num in nums:
        freq_map[num]= 1+ freq_map.get(num,0)
    #populate bucket
    for key,value in freq_map.items():
        freq[value].append(key)
    
    #for loop in descending order
    res=[]
    for i in range(len(freq)-1,0,-1):
        for value in freq[i]:
            res.append(value)
            if len(res)==k:
                return res

print(topKArray([1, 1, 1, 2, 2, 3], 2))
