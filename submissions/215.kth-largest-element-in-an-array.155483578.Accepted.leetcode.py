class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right):
            pivot = nums[left]
            i = left + 1
            j = right

            while(i <= j):
                if nums[i] >= pivot:
                    i += 1
                    continue
                if nums[j] < pivot:
                    j -= 1
                    continue
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

            nums[left] = nums[j]
            nums[j] = pivot
            return j

        def select(left, right):
            pivot = partition(left, right)
            if pivot + 1 == k:
                return nums[pivot]
            elif pivot + 1 > k:
                return select(left, pivot - 1)
            else:
                return select(pivot + 1, right)

        return select(0, len(nums) - 1)
