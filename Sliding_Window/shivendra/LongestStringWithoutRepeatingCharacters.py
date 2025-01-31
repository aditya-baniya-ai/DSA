def lengthOfLongestSubstring(s):
        l = 0
        sett = set() #use set to store unique elements and to .add, .remove
        longest = 0

        for r in range(len(s)):
            while s[r] in sett: #check if duplicate is present
                sett.remove(s[l])
                l += 1 #increment of pointer l
            sett.add(s[r])
            window_length = (r-l) + 1
            longest = max (longest, window_length)
            
        return longest
print(lengthOfLongestSubstring("abcabcbb"))
        
