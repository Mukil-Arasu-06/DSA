def sortedSquares(nums):
    left = 0
    right = len(nums)-1

    result = [0] * len(nums)

    for position in range(len(nums)-1,-1,-1):

        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] ** 2
            left += 1
        else:
            result[position] = nums[right] ** 2
            right -=1 

    return result 


#     Full Iteration Flow

# Input:

# nums = [-4, -1, 0, 3, 10]

# Initial:

# left = 0
# right = 4


# result = [0, 0, 0, 0, 0]

# Visual:

#         left               right
#          ↓                   ↓
# nums = [-4,  -1,   0,   3,  10]
# Iteration 1
# position = 4

# Compare:

# abs(nums[left])
# = abs(-4)
# = 4


# abs(nums[right])
# = abs(10)
# = 10

# So:

# 10 > 4

# Take 10.

# Square:

# 10² = 100

# Put it at position 4.

# result = [0, 0, 0, 0, 100]

# Move right:

# left = 0
# right = 3
# Iteration 2

# Now:

#          left          right
#           ↓              ↓
# nums = [-4, -1,  0,  3, 10]

# Compare:

# abs(-4) = 4
# abs(3)  = 3

# 4 > 3, so take -4.

# Square:

# (-4)² = 16

# Put it at position 3.

# result = [0, 0, 0, 16, 100]

# Move left:

# left = 1
# right = 3
# Iteration 3
#             left       right
#              ↓          ↓
# nums = [-4, -1,  0,  3, 10]

# Compare:

# abs(-1) = 1
# abs(3)  = 3

# 3 > 1, so take 3.

# Square:

# 3² = 9

# Put at position 2.

# result = [0, 0, 9, 16, 100]

# Move right:

# left = 1
# right = 2
# Iteration 4
#           left   right
#            ↓      ↓
# nums = [-4, -1,  0,  3, 10]

# Compare:

# abs(-1) = 1
# abs(0)  = 0

# 1 > 0, so take -1.

# Square:

# (-1)² = 1

# Put at position 1.

# result = [0, 1, 9, 16, 100]

# Move left:

# left = 2
# right = 2
# Iteration 5

# Now both pointers are at 0:

#              ↓
# nums = [-4, -1,  0,  3, 10]
#              ↑
#            left/right

# Compare:

# abs(0) = 0
# abs(0) = 0

# Take the right side because of else.

# 0² = 0

# Put at position 0.

# result = [0, 1, 9, 16, 100]

# Move:

# right = 1

# Loop ends.