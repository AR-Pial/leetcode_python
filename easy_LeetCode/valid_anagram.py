class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in s:
            count_s[i] = 1 + count_s.get(i, 0)

        for i in t:
            count_t[i] = 1 + count_t.get(i,0)

        if count_s != count_t:
            return False

        return True


s = "anagram"
t = "nagaram"
sol = Solution()
res = sol.isAnagram(s,t)

print(res)