class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = {}
        for c in magazine:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        for c in ransomNote:
            if c not in char_count:
                return False
            elif char_count[c] == 1:
                del char_count[c]
            else:
                char_count[c] -= 1
        return True

ransomNote = "aa"
magazine = "aab"
sol = Solution()
res = sol.canConstruct(ransomNote, magazine)
print(res)
