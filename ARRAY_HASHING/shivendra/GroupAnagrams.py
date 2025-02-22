from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict with a default value of an empty list.
        # This dictionary will map each sorted word (as a string) to a list of words that are anagrams.
        d = defaultdict(list)

        # Iterate over each word in the input list.
        for word in strs:
            # Sort the characters of the word.
            # sorted(word) returns a list of characters sorted in ascending order.
            sorted_chars = sorted(word)
            # Join the sorted characters back into a string.
            sorted_word = ''.join(sorted_chars)
            # Use the sorted word as a key and append the original word to its list.
            d[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists.
        return list(d.values())
