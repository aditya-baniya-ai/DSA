
def isValidAnagram(s,t):
    if len(s) != len(t):
        return 
    
    dict1,dict2={},{}
    
    for num in s:
        dict1[num] = 1+ dict1.get(num,0)
    for num in t:
        dict2[num] = 1+ dict2.get(num,0)
    
    return dict1==dict2

print(isValidAnagram("woow","wwoo"))


