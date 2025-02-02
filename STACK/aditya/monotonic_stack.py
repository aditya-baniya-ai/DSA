def nextGreaterElement(array):
    stack = []
    nge = [0]*len(array)
    i = len(array)-1
    
    while i>=0:
        while stack and (stack[-1] <= array[i]):
            stack.pop()
            
        if not stack:
            nge[i]  = -1
        else:
            nge[i] = stack[-1]    
        stack.append(array[i])
        i-=1
        
    return nge
    
    
print(nextGreaterElement([1,3,4,2]))