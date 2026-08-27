from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 
        right = len(s)-1

        while left < right :
            s[left],s[right] = s[right],s[left]

            left += 1
            right -=1 






# Full iteration flow

# Initial:

# s = ["h", "e", "l", "l", "o"]

# left = 0
# right = 4

# Visual:

#        left             right
#          ↓                ↓
# ["h", "e", "l", "l", "o"]
# Iteration 1

# Check:

# left < right
# 0 < 4 ✅

# Swap:

# s[left], s[right] = s[right], s[left]

# So:

# h ↔ o

# Array becomes:

# ["o", "e", "l", "l", "h"]

# Move pointers:

# left += 1
# right -= 1

# Now:

# left = 1
# right = 3

# Flow:

# ["o", "e", "l", "l", "h"]
#       ↑          ↑
#     left       right
# Iteration 2

# Check:

# 1 < 3 ✅

# Current:

# left  → "e"
# right → "l"

# Swap:

# e ↔ l

# Array:

# ["o", "l", "l", "e", "h"]

# Move:

# left = 2
# right = 2

# Now:

# ["o", "l", "l", "e", "h"]
#           ↑
#        left/right
# Iteration 3

# Check:

# left < right
# 2 < 2 ❌

# So the loop stops.

# Final:

# ["o", "l", "l", "e", "h"]
