class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            # print(f"{stack=}, evaluating {i=}, {s[i]=}")
            # find the rest of the number
            if s[i].isdigit():
                temp_amount = ""
                while i < n and s[i].isdigit():
                    temp_amount += s[i]
                    i += 1
                # print(f"found number, adding {temp_amount=}")
                stack.append(temp_amount)
            # find the rest of the string
            elif s[i].isalpha():
                temp_str = ""
                while i < n and s[i].isalpha():
                    temp_str += s[i]
                    i += 1
                # print(f"found letter, adding {temp_str=}")
                stack.append(temp_str)
            # compute everything until the first number
            elif s[i] == "]":
                temp_str = ""
                while len(stack) > 0 and stack[-1].isalpha():
                    temp_str = stack.pop() + temp_str
                # should be a number now
                amount = stack.pop()
                if amount.isdigit():
                    combined = int(amount) * temp_str
                    # print(f"doing the math, {combined=}")
                    stack.append(combined)
                else:
                    raise Exception("missing number")
                i += 1
            elif s[i] == "[":
                # print(f"skipping open bracket")
                i += 1
            else:
                raise Excpetion("unexpected character")
                
        # print(f"{stack=}")
        return "".join(stack)
        