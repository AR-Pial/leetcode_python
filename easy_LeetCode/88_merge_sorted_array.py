def merge(nums1, m, nums2, n):
    le = m + n - 1
    nm = m - 1
    nn = n - 1
    while nm >= 0 and nn >= 0:
        if nums1[nm] > nums2[nn]:
            nums1[le] = nums1[nm]
            nm -= 1
        else:
            nums1[le] = nums2[nn]
            nn -= 1
        le -= 1

    if nn >= 0:
        nums1[:nn + 1] = nums2[:nn + 1]
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
result = merge(nums1, m, nums2, n)
print(result)