def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        new_list= []
        nums1_count = 0
        nums2_count = 0
        nums1 = [x for x in nums1 if x != 0]
        nums2 = [x for x in nums2 if x != 0]

        for i in range(m+n):
            if nums1_count == m:
                new_list += nums2[nums2_count:]
                break
            elif nums1_count == n:
                new_list += nums1[nums1_count:]
                break

            if nums1[nums1_count] < nums2[nums2_count]:
                new_list.append(nums1[nums1_count])
                nums1_count += 1
            else:
                new_list.append(nums2[nums2_count])
                nums2_count += 1
        
        nums1 = new_list
        print(nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)

1
1,2
1,2,2
1,2,2,3