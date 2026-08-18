# my solution 
def removeElement(nums, val) -> int :
    insert_pos = 0
    for num in nums:
        if num != val:
            nums[insert_pos] = num
            insert_pos += 1
    
    k = insert_pos

    # while insert_pos < len(nums):
    #     nums[insert_pos] = '_'
    #     insert_pos += 1

    return k

nums = [3,2,2,3]
val = 3

ans = removeElement(nums,val)
print(ans)


#chatGpt solution 

class Solution:
    def removeElement(self, nums, val):
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j