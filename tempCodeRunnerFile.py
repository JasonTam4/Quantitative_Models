for i in range(len(nums)):
        if nums[i] == val:
            count += 1
            for j in range(len(nums) - i - 1):
                nums[j] = nums[j+1]