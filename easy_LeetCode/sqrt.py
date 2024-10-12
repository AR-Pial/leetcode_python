# def mySqrt(x):
#     if x == 0 or x == 1:
#         return x
#     else:
#         i = 2
#         while i <= x:
#             square = i * i
#             if square > x:
#                 return i-1
#             i += 1
def mySqrt(x):
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        mid_sq = mid * mid
        if mid_sq == x:
            return mid
        elif mid_sq < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

result = mySqrt(8)
print(result)
