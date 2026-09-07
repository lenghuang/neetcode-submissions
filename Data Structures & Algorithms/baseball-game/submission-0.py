class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                if len(scores) < 2:
                    print(f"invalid operation {op=}")
                    return -1
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                if len(scores) < 1:
                    print(f"invalid operation {op=}")
                    return -1
                scores.append(2 * scores[-1])
            elif op == "C":
                if len(scores) < 1:
                    print(f"invalid operation {op=}")
                    return -1
                _ = scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)