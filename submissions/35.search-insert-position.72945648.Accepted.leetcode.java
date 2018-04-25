public class Solution
{
    public int searchInsert(int[] nums, int target)
    {
        int left = 0;
        int right = nums.length - 1;

        while (left + 1 < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] < target)
            {
                left = mid;
            }
            else
            {
                right = mid;
            }
        }

        if (nums[left] >= target)
        {
            return left;
        }
        else if (nums[right] >= target)
        {
            return right;
        }
        else
        {
            return right + 1;
        }
    }
}

