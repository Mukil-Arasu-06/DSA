#LeetCode 283 — Move Zeroes

def moveZeroes(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


# Step 2: First for loop iteration
# 1	0	0	0 != 0 ❌	Nothing	[0,1,0,3,12]
# 2	1	0	1 != 0 ✅	nums[0] = 1	[1,1,0,3,12]
# 3	0	1	0 != 0 ❌	Nothing	[1,1,0,3,12]
# 4	3	1	3 != 0 ✅	nums[1] = 3	[1,3,0,3,12]
# 5	12	2	12 != 0 ✅	nums[2] = 12	[1,3,12,3,12]
