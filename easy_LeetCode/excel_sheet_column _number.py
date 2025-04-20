class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            result = result * 26 + val
        return result

columnTitle = "AZ"
sol = Solution()
result = sol.titleToNumber(columnTitle)
print(result)