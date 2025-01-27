from collections import defaultdict
# this means matching key:value pair will be string:list pair
# best solution

def anagrams(strs):
    dictionary = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        dictionary[sorted_word].append(word)
        
    return list(dictionary.values())
        
    
print(anagrams(["tan","ant","nta","ate","tea","bat","",""]))