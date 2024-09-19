nums = [0,0,1,1,1,2,2,3,3,4]
num_len = len(nums)
j = 0
for i in range(1, num_len):
    if nums[i] > nums[j]:
        j = j+1
        nums[j] = nums[i]

print(j, "Num : ",nums)
