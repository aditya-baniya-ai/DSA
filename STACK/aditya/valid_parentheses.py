""" 
    First check if we see open parentheses in the s string and append in the stack
    then we check if the parentheses is not the open one, then we pop from the stack and check with the pair dictionary
    pair dictionary is designed in such a way that if the string is closing one then we check the value of the closing bracket in dict and match that
    
"""

def isValid(s):
    stack = []
    pair = {'}':"{", "]":"[", ")":"("}

    for i in range(len(s)):
        if s[i] in "[{(":
            stack.append(s[i])

        else:
            if stack:
                if stack.pop() != pair[s[i]] :
                    return False

            else:
                return False # if stack if empty we return false

    return not stack

    
    
            
            
print(isValid("()"))
