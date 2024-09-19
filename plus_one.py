def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        num = digits[i] + 1
        if num == 10:
            if i != 0:
                digits[i] = 0
            else:
                digits[i] = 0
                digits.insert(0, 1)
                return digits
        else:
            digits[i] = num
            return digits


digits = [1, 9, 8]
result = plusOne(digits)
print(result)
