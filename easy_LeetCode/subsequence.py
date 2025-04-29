class Solution(object):
    def isSubsequence(self, s, t):

        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

s = "abc"
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s,t)
print(res)
