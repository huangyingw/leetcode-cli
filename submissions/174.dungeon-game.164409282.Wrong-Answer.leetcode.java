public class Solution
{
    public int calculateMinimumHP(int[][] dungeon)
    {
        int m = dungeon.length, n = dungeon[0].length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 0);

        for (int i = m - 1; i >= 0; i--)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                System.out.printf("Math.min(dp[j], dp[j + 1]) --> %s\n", Math.min(dp[j], dp[j + 1]));
                System.out.printf("Math.min(dp[j], dp[j + 1]) - dungeon[i][j] --> %s\n", Math.min(dp[j], dp[j + 1]) - dungeon[i][j]);
                dp[j] = Math.max(1, Math.min(dp[j], dp[j + 1]) - dungeon[i][j]);
                System.out.printf("dp[%s] --> %s\n", j, dp[j]);
            }

            System.out.printf("\n");
        }

        return dp[0];
    }
}

