class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_brackets = { ")" : "(", "}" : "{", "]" : "[" }
        open_brackets = set(close_brackets.values())
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if c in close_brackets and len(stack) > 0 and close_brackets[c] == stack[-1]:
                    _ = stack.pop()
                else:
                    return False
        return len(stack) == 0