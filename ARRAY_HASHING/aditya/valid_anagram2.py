#changes made to file
from collections import Counter

def valid_anagram(s,t):
    freq1 = Counter(s)
    freq2 = Counter(t)
    
    return freq1==freq2

print(valid_anagram("anagram", "nagaram"))