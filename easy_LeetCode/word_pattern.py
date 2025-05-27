class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        ctw = {}
        wtc = {}
        if len(pattern) != len(words):
            return False
        for c, w in zip(pattern,words):
            if c in ctw and ctw[c] != w:
                return False
            if w in wtc and wtc[w] != c:
                return False
            ctw[c] = w
            wtc[w] = c

        return True

pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
res = sol.wordPattern(pattern,s)
print(res)