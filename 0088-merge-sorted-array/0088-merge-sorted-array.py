class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_nums1 = m - 1  # pointer for nums1
        ptr_nums2 = n - 1  # pointer for nums2
        placement_idx = m + n - 1  # pointer for ele placement in nums1

        while ptr_nums1 >= 0 and ptr_nums2 >= 0:
            if nums1[ptr_nums1] > nums2[ptr_nums2]:
                nums1[placement_idx] = nums1[ptr_nums1]
                ptr_nums1 -= 1
            else:
                nums1[placement_idx] = nums2[ptr_nums2]
                ptr_nums2 -= 1
            placement_idx -= 1 # move placement_idx to -1 position

        # If there are remaining elements in nums2, copy them
        while ptr_nums2 >= 0:
            nums1[placement_idx] = nums2[ptr_nums2]
            ptr_nums2 -= 1
            placement_idx -= 1