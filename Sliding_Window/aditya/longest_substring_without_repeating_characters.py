""""
    Logic: first we have a set to collect unique elements and a max_number to store the length of maximum string so far
    for loop: runs from 0 to len(s). We check if s[right] in Charset, if not we add there and find the maxNumber so far
    if it is in charSet we run a while loop until we remove that repeated character from the charSet
"""

def longCharWithoutRepeat(s):
    left = 0
    charSet=set()
    max_number=0
    
    for right in range(len(s)):
        if s[right] not in charSet:
            charSet.add(s[right])
            max_number = max(max_number,right-left+1)
            
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
                
    return max_number



print(longCharWithoutRepeat("abcabc"))