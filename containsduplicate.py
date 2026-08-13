class containsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            else:
                seen.add(num)
        return False


nums = [1, 2, 3, 4, 5,3]
duplicate_checker = containsDuplicate()
result = duplicate_checker.containsDuplicate(nums)
print("Contains duplicate:", result)

        