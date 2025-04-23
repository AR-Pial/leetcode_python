class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, l = len(s) - 1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            l += 1
            i -= 1
        return l

s = "   fly me   to   the moon  "
sol = Solution()
res = sol.lengthOfLastWord(s)
print(res)