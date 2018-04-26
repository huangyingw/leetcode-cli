public class Solution
{
    public void rotate(int[] nums, int k)
    {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
    public void reverse(int[] nums, int left, int right)
    {
        for (; left < right; left++, right--)
        {
            int temp = nums[right];
            nums[right] = nums[left];
            nums[left] = temp;
        }
    }
}
