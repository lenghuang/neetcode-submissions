class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []
        
        if s[0] != "#":
            return []

        i = 1 # start at the separator 
        res = []
        while i < len(s):
            res_str = ""
            
            # first get the number value
            j = i
            while j < len(s) and s[j] != "#":
                j += 1

            str_len = int(s[i:j])
            
            j += 1 # move past separator
            k = j + str_len # then get the string after

            res.append(s[j:k])
            i = k + 1 # move past separator

        return res
