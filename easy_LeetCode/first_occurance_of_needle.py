# Method 2
def strStr(haystack, needle):
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1



# Method 1
# def strStr(haystack, needle):
#     if len(needle) > len(haystack):
#         return -1
#
#     else:
#         for i in range(len(haystack) + 1 - len(needle)):
#             for j in range(len(needle)):
#                 if haystack[i + j] != needle[j]:
#                     break
#                 if j == len(needle) - 1:
#                     return i
#         return -1

haystack = "mississippi"
needle = "issip"

r = strStr(haystack,needle)
print(r)



