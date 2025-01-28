from collections import defaultdict
# this means matching key:value pair will be string:list pair
# best solution
# 

def anagrams(strs):
    dictionary = defaultdict(list) # string:list pair
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        dictionary[sorted_word].append(word)
        #list.append(word)
        #dictionary[sorted_word] refers to a list and now we will append words to that list
        
    return list(dictionary.values())
        
    
print(anagrams(["tan","ant","nta","ate","tea","bat","",""]))