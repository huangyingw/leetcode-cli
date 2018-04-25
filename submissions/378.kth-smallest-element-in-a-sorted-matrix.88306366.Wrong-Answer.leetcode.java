public class Solution 
{
    public int kthSmallest(int[][] matrix, int k) 
    {
        int m = matrix.length;
        int lower = matrix[0][0];
        int upper = matrix[m - 1][m - 1];
        int mid = 0;
 
        while (lower + 1 < upper)
        {
            mid = (lower + upper) / 2;
            int count = count(matrix, mid);
     
            if (count > k)
            {
                upper = mid;
            }
            else
            {
                lower = mid;
            }
        }
 
        return lower == mid ? lower : upper;
    }
 
    private int count(int[][] matrix, int target)
    {
        int m = matrix.length;
        int i = m - 1;
        int j = 0;
        int count = 0;
 
        while (i >= 0 && j < m)
        {
            if (matrix[i][j] <= target)
            {
                count += i + 1;
                j++;
            }
            else
            {
                i--;
            }
        }
 
        return count;
    }
}
