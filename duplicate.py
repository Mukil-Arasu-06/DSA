def containsDuplicate(nums):
    num_map = {}
    for num in nums:
        if num in num_map:
            return True
        num_map[num] = 1
    return False
nums=[2,3,4,5,5]

print(containsDuplicate(nums))
