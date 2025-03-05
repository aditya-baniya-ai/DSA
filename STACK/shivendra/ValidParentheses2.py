
def isValid(s):
    stack = []
    for char in s:
        if char=='(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char =='}' or char == ']':
            if char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            else: 
                return False
    return not stack