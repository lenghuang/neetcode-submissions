'''
1. Write out the happy path example

stack = [1,2,+] 
i see +, i know i need 2, so i pop 2

add 2, and put it back on the stack,

stack = [3]

push 3

stack = [3,3], then i get *, pop + push

stack = 9, get 4, then - , which leaves me with 5

2. Pause and reflect after writing
'''

class Solution:
    
    operators = set(["+", "-", "*", "/"])

    def operate(self, token: str, x: int, y: int) -> int:      
        match token:
            case "+":
                return x + y
            case "-":
                return y - x
            case "*":
                return x * y
            case "/":
                return y / x
            case _:
                raise ValueError("Invalid Token")
            
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in self.operators:
                x = stack.pop()
                y = stack.pop()
                result = self.operate(t, x, y)
                stack.append(int(result))
            else:
                stack.append(int(t))

        return stack[-1]
        