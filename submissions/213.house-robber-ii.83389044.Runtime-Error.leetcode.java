public class Solution 
{
    public int rob(int[] nums) 
    {
        if(nums.length == 1)
        {
            return nums[0];
        }
        
        if(nums.length == 2)
        {
            return Math.max(nums[0], nums[1]);    
        }
        
        return Math.max(rob1(nums, 0, nums.length - 2), rob1(nums, 1, nums.length - 1));    
    }
    
    public int rob1(int[] nums, int start, int end)
    {
        int[] dp = new int[end - start + 2];
        dp[0] = 0;
        dp[1] = nums[start];
        
        for(int i = 2; i <= end - start + 1; i++)
        {
            dp[i] = Math.max(dp[i - 2] + nums[start + i - 1], dp[i - 1]);    
        }
        
        return dp[end - start + 1];
    }
}
