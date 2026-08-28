class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def log(*args):
            if False:
                print(*args)

        # loop through and create windows
        # if need to replace <= k, keep adding
        # if need to replace > k, reset until its no longer the case
        # track max window size throuhgout this process

        maxStrLen = 0
        # needToReplace = 0
        # maxFreqChar = None
        dict = {}

        # init freq
        for c in s:
            dict[c] = 0

        dict[s[0]] = 1

        # window stuff
        prev = 0
        i = 0

        while i < len(s):
            log("---")
            log("prev", prev, "i", i, "substr", s[prev:i+1])
            # update freq

            # find the char with most freq
            maxFreq = 0
            for c, freq in dict.items():
                maxFreq = max(maxFreq, freq)
            log("maxFreq", maxFreq, "dict", dict)
            # the window size - maxFreqChar should be how many things you need to replace!
            windowSize = i - prev + 1
            needToReplace = windowSize - maxFreq
            log("windowSize", windowSize, "needToReplace", needToReplace)
            if (needToReplace > k):
                log("case a")
                dict[s[prev]] -= 1
                prev += 1
            else:
                log("case b")
                i += 1
                maxStrLen = max(windowSize, maxStrLen)
                if i < len(s):
                    dict[s[i]] += 1

        return maxStrLen