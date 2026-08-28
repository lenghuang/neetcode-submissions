class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # The key observation is that you must always have more opens than close parens
        # So we can brute force by adding either "(" or ")" and checking if is valid
        # Let n be the number of open parentheses

        # base case n = 0, [""]
        # base case n = 1, ["()"]
        # f(n, open_count, close_count) =
        #   if count of open_count > close_count of close
        #   try adding another open
        #   also try adding a close count

        parens = set()

        def recurse(o, c, acc):
            if o == n and c == n:
                parens.add(acc)
                return
            if o < n:
                recurse(o + 1, c, acc + "(")
            if c < o:
                recurse(o, c + 1, acc + ")")

        recurse(0, 0, "")
        return list(parens)