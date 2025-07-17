def characterReplacement(s, k):
        l = 0
        longest = 0
        count = {} #hashmap to store counts of each element

        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r], 0)
            window_length = r - l + 1

            #if len of window - highest freq <= k: it is a valid replacement!
            if window_length - max(count.values()) <= k:
                longest = max (longest, window_length)

            else: #if it is > k: remove the leftmost character and slide the l pointer
                count[s[l]] -= 1
                l += 1

        return longest
                
print(characterReplacement("AABABBA",1))
