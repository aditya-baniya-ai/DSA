def validPalindrome(s):

    l,r=0,len(s)-1
    s = s.lower()

    while l<r:

        while l<r and not s[l].isalnum(): #donot forget checking bounds
            l+=1

        while r>l and not s[r].isalnum():
            r-=1

        if s[l] != s[r]: #donot forget to lowercase letters
            return False
        
        #Regular pointer sliding
        l+=1
        r-=1
    # If not false, at the end of the loop-TRUE
    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))