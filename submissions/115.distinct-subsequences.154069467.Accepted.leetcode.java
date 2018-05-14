public class Solution
{
    public int numDistinct(String S, String T)
    {
        int[][] dp = new int[S.length() + 1][T.length() + 1];
        dp[0][0] = 1;

        for (int i = 1; i <= S.length(); i++)
        {
            dp[i][0] = 1;

            for (int j = 1; j <= T.length(); j++)
            {
                if (T.charAt(j - 1) == S.charAt(i - 1))
                {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                }
                else
                {
                    dp[i][j] =  dp[i - 1][j];
                }
            }
        }

        return dp[S.length()][T.length()];
    }
}

