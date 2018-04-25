public class Solution
{
    public int coinChange(int[] coins, int amount)
    {
        int dp[] = new int[amount + 1];
        dp[0] = 0;

        for (int i = 1; i <= amount; i++)
        {
            dp[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i <= amount; i++)
        {
            for (int j = 0; j < coins.length; j++)
            {
                if (i - coins[j] >= 0)
                {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }

                System.out.println("i --> " + i);
                System.out.println("dp[i] --> " + dp[i]);
                System.out.println("coins[j] --> " + coins[j]);
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}
