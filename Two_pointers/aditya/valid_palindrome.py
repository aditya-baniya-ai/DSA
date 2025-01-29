def valid_palindrome(s):
    s = ''.join(s.split()).lower()
    s=''.join(filter(str.isalnum,s))
    i=0
    j=len(s)-1
    print(s)

    while i<=j:
        if s[i] != s[j]:
            return False

        i+=1
        j-=1

    return True
print(valid_palindrome("A man, a plan, a canal: Panama"))