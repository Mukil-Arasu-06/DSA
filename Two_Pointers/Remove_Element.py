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





        Sure. For nums = [3, 2, 2, 3] and val = 3, here is the iteration clearly:

Iteration	i	nums[i]	Check nums[i] != val	j before	Action	nums after	j after
1	0	3	3 != 3 ❌	0	Skip	[3, 2, 2, 3]	0
2	1	2	2 != 3 ✅	0	nums[0] = 2	[2, 2, 2, 3]	1
3	2	2	2 != 3 ✅	1	nums[1] = 2	[2, 2, 2, 3]	2
4	3	3	3 != 3 ❌	2	Skip	[2, 2, 2, 3]	2