class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            val_a = (ord(a[i]) - ord("0")) if i < len(a) else 0
            val_b = (ord(b[i]) - ord("0")) if i < len(b) else 0
            sum = val_a + val_b + carry
            c = str(sum % 2)
            res = c + res
            carry = sum // 2

        if carry:
            res = "1" + res
        return res

a = "1010"
b = "1011"
sol = Solution()
res = sol.addBinary(a, b)
print(res)
