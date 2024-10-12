def climbStairs(n):
      one_step = 1
      two_step = 1

      for i in range(n-1):
         temp = one_step
         one_step = one_step + two_step
         two_step  = temp

      return one_step


result = climbStairs(5)
print(result)