s = "({})"
open_bracket = ["(", "{", "["]
close_bracket = [")", "}", "]"]
ob = []
result = True
for ch in s:
   if ch in open_bracket:
       ob.append(ch)
   else:
       c_index = close_bracket.index(ch)
       if ob:
            last_obr = ob[-1]
       else:
           result = False
           break
       o_index = open_bracket.index(last_obr)
       if c_index == o_index:
           ob.pop()
       else:
           result = False
           break

if ob:
    result = False

print(result)

