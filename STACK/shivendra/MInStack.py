def __init__(self):
        self.stack = []
        self.minStack = []
        
#donot forget sel. and checking for minStack
def push(self, val: int) -> None:
        self.stack.append(val)
        val= min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
#Donot forget return
def top(self) -> int:
        return self.stack[-1]
        

def getMin(self) -> int:
        return self.minStack[-1]

