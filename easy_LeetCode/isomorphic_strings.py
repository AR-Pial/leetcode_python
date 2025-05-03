class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stt, tts = {}, {}
        for i,j in zip(s,t):
            if ((i in stt and stt[i] != j) or
                (j in tts and tts[j] != i)):
                return False
            stt[i] = j
            tts[j] = i

        return True


s = "egg"
t = "add"
sol = Solution()
res = sol.isIsomorphic(s,t)
print(res)