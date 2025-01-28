from collections import defaultdict
def top_k(nums,k):
    dictionary = defaultdict(int)
    count = 0
    answer = []
    
    for i in nums:
        dictionary[i]+=1
        
    val_based_rev = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    
    for i in range(k):
        answer.append(list(val_based_rev)[count])
        count+=1
        
    return answer
    
    
    
print(top_k([1,1,1,2,2,3],2))