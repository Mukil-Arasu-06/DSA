

def removeDuplicates(nums):
    if not nums:
        return 0
    left = 0
    for right in range(1,len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

    return left +1 

nums=[1,1,2,2,3] 

ans = removeDuplicates(nums)
print(ans)


# Input:

# nums = [1, 1, 2, 2, 3]
# Iteration 1
# left = 0
# right = 1


# nums[left]  = nums[0] = 1
# nums[right] = nums[1] = 1

# Check:

# 1 != 1  → False

# So nothing changes.

# [1, 1, 2, 2, 3]
#  ↑  ↑
#  L  R
# Iteration 2
# left = 0
# right = 2


# nums[left]  = 1
# nums[right] = 2

# Check:

# 1 != 2 → True

# So:

# left += 1

# Now:

# left = 1

# Then:

# nums[left] = nums[right]

# means:

# nums[1] = nums[2]
# nums[1] = 2

# Array becomes:

# [1, 2, 2, 2, 3]
#     ↑  ↑
#     L  R
# Iteration 3
# left = 1
# right = 3


# nums[left]  = 2
# nums[right] = 2

# Check:

# 2 != 2 → False

# Nothing changes.

# [1, 2, 2, 2, 3]
#     ↑     ↑
#     L     R
# Iteration 4
# left = 1
# right = 4


# nums[left]  = 2
# nums[right] = 3

# Check:

# 2 != 3 → True

# Move left:

# left = 2

# Copy:

# nums[2] = nums[4]
# nums[2] = 3

# Array:

# [1, 2, 3, 2, 3]
#        ↑     ↑
#        L     R
# Final result
# left = 2

# So:

# k = left + 1
# k = 3

# The first 3 positions contain the unique values:

# [1, 2, 3, 2, 3]
#  └─────┘
#  [1, 2, 3]

# Main thing to remember:

# right → searches
# left  → stores unique values

# That's the core Two Pointer idea in this problem.