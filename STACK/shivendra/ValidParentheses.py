def isValid(str):
        #Create a hashmap with brackets and if, if, else, else rule
        #True if returns empty list #.pop,.append
        list = []
        d = {')':'(', '}':'{', ']':'['}

        for char in str:
            if char in d:
                if list and list[-1] == d[char]:
                    list.pop()
                else: 
                    return False
            else: 
                list.append(char)
                
        return not list
print(isValid("()[]{}"))