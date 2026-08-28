'''

stack = [1,2,0]
minStack = [1,0]

getMin() -> 0 since its top of minStack

pop, remove 0 from stack, and from minStack since its there

stack = [1,2]
minStack = [1]

top gets me top of stack 2 
minStack gets me top of min stack 1

["MinStack", "push", -2, "push", -2, "push", -3, "push", -3, "getMin", "pop", "getMin"]

push -2
stack = [-2]
minStack = [-2]

push -2
stack = [-2,- 2]
minStack = [-2, -2]

push -3
stack = [-2,- 2, -3]
minStack = [-2, -2, -3]

push -3
stack = [-2,- 2, -3, -3]
minStack = [-2, -2, -3, -3]

get min -3
pop 
get min -3? 

'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Add if smaller than what's on top of min stack 
        if len(self.minStack) > 0 and val <= self.minStack[-1]:
            self.minStack.append(val)
        # Or if empty
        elif len(self.minStack) == 0:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        
        # Add if its whats on top of min stack, pop that too
        if len(self.minStack) > 0 and val == self.minStack[-1]:
            _ = self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
