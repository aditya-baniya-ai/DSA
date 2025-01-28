# if (n-1) exists, it cannot be the begining of the sequence, so we ignore it
# and only care about the num for which (n-1) doesn't exist

def longestSequence(nums):
    numSet=set(nums) # Important to avoid duplicates and redundancies
    longest=0 # MUST initialize the variable
    for n in numSet:
        if (n-1) not in numSet:
            length =1
            while (n+length) in numSet:
                length += 1 
            longest = max(longest, length)

    return longest

print(longestSequence([100,4,200,1,3,2]))
print(longestSequence([0,3,7,2,5,8,4,6,0,1]))
#time complexity: O(n)