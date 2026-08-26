class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


s = "A man, a plan, a canal: Panama"


# Initial
# left = 0
# right = len(s) - 1

# So:

# left  → A
# right → a
# Iteration 1
# Step 1 — Check left
# s[left]

# is:

# A

# A is a letter, so don't skip it.

# Step 2 — Check right

# Right character is:

# a

# It's also a letter.

# Step 3 — Compare
# s[left].lower() != s[right].lower()

# Becomes:

# 'a' != 'a'

# False.

# So they match ✅

# Step 4 — Move pointers
# left += 1
# right -= 1

# Now:

# left  → index 1 → space
# right → previous character
# Iteration 2

# Left is:

# space

# This is not alphanumeric.

# So:

# while left < right and not s[left].isalnum():
#     left += 1

# moves left.

# left: index 1 → index 2

# Now:

# left → m

# Right is still at:

# a

# Compare:

# m vs a

# Wait — this would look wrong if we only consider the visible beginning/end. But remember the actual string's right side is being processed symmetrically; the important point is that after skipping the space, the next valid character from the left is m, while the next valid character from the right is m.

# So the comparison is:

# m == m ✅

# Move:

# left += 1
# right -= 1
# Iteration 3

# Pointers reach:

# left  → a
# right → a

# Compare:

# a == a ✅

# Move both.

# Iteration 4

# They reach:

# left  → n
# right → n

# Compare:

# n == n ✅

# Move both.

# Iteration 5

# The left pointer reaches:

# ,

# Comma is not alphanumeric.

# So:

# not s[left].isalnum()

# is True.

# Move:

# left → next character

# The right pointer also skips punctuation/spaces whenever it encounters them.

# Eventually the next valid characters are compared.

# What the loop is doing

# The actual process is always:

# 1. Check left
#        ↓
# 2. If space/punctuation → move left
#        ↓
# 3. Check right
#        ↓
# 4. If space/punctuation → move right
#        ↓
# 5. Compare both characters
#        ↓
# 6. Different → False
#        ↓
# 7. Same → move both pointers
#        ↓
# 8. Repeat
# Easier example for FULL iteration

# Let's use:

# s = "A man a"

# Ignore spaces and capitalization.

# Valid characters:

# A m a n a
# Initial
# left = 0 → A
# right = 6 → a

# Compare:

# A → a
# a == a ✅

# Move:

# left = 1
# right = 5
# Iteration 2
# left → m
# right → space

# Right is not alphanumeric.

# Skip it:

# right = 4

# Now:

# left → m
# right → a

# Compare:

# m != a ❌

# Return:

# False
# Why .isalnum()?
# s[left].isalnum()

# checks whether the character is:

# a letter → True
# a number → True
# space → False
# comma → False
# : → False
# ! → False

# Example:

# "A".isalnum()     # True
# "5".isalnum()     # True
# " ".isalnum()     # False
# ",".isalnum()     # False
# Why .lower()?

# Because:

# A
# a

# should be treated as the same character.

# "A".lower()

# gives:

# "a"

# So:

# if s[left].lower() != s[right].lower():

# compares them without caring about uppercase/lowercase.

# Main Two-Pointer Pattern

# Remember this:

# left →→→

# " A m a n a m A "
#   ↑             ↑
#  left          right

# ←←← right

# We:

# skip unwanted characters
#         ↓
# compare left and right
#         ↓
# same? → move both
#         ↓
# different? → False
#         ↓
# pointers meet → True
# Complexity
# Time:  O(n)
# Space: O(1)