def mySqrt(x):
    if x == 0 or x == 1:
        return x
    else:
        i = 2
        while i <= x:
            square = i * i
            if square > x:
                return i-1
            i += 1


result = mySqrt(8)

print(result)
