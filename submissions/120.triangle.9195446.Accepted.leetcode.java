public class Solution
{
    public int minimumTotal(List<List<Integer>> triangle)
    {
        int rows = triangle.size();
        int[] dp = new int[rows];

        for (int i = 0; i < rows; i++)
        {
            dp[i] = triangle.get(rows - 1).get(i);
        }

        for (int i = rows - 2; i >= 0; i--)
            for (int j = 0; j <= i; j++)
            {
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j], dp[j + 1]);
            }

        return dp[0];
    }
}
