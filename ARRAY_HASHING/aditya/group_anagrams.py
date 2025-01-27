from collections import defaultdict
# it provides a default value for the key that does not exist and never raises a Keyerror

def group_anagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord("a")] +=1
            
        res[tuple(count)].append(s)
    
    return res.values()


        
        
    