nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            k -= 1

    for i in range(len(nums) - k):  
        nums.remove(val)

    print(nums)
removeElement(nums, val)