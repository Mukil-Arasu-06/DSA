class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1


# Let's completely trace:

# numbers = [2, 7, 11, 15]
# target = 9
# Initial
# left = 0
# right = 3

# Array:

# [2, 7, 11, 15]
#  ↑           ↑
#  L           R
# Iteration 1
# current_sum = numbers[left] + numbers[right]

# So:

# 2 + 15 = 17

# Compare:

# 17 == 9  ❌
# 17 <  9  ❌
# 17 >  9  ✅

# Therefore:

# right -= 1

# Now:

# left = 0
# right = 2
# Iteration 2
# [2, 7, 11, 15]
#  ↑        ↑
#  L        R

# Calculate:

# 2 + 11 = 13

# Compare:

# 13 == 9 ❌
# 13 <  9 ❌
# 13 >  9 ✅

# Therefore:

# right -= 1

# Now:

# left = 0
# right = 1
# Iteration 3
# [2, 7, 11, 15]
#  ↑     ↑
#  L     R

# Calculate:

# 2 + 7 = 9

# Compare:

# 9 == 9 ✅

# Found!

# Python returns:

# [left + 1, right + 1]

# Therefore:

# [1, 2]