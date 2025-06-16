class Solution:
    def mergeCount(self, nums, left, mid, right):
        count = 0
        j = mid + 1

        # Count reverse pairs
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)

        # Merge two sorted parts
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1

        # Copy back to original array
        for k in range(len(temp)):
            nums[left + k] = temp[k]

        return count

    # 2️ mergeSort function
    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        count = 0
        count += self.mergeSort(nums, left, mid)
        count += self.mergeSort(nums, mid + 1, right)
        count += self.mergeCount(nums, left, mid, right)

        return count

    # 3 main reversePairs function
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)    