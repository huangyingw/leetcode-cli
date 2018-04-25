  public class Solution
  {
    public int findMin(int[] num)
    {
      return findMin(num, 0, num.length - 1);
    }

    public int findMin(int[] num, int start, int end)
    {
      if ((end - start) <= 1)
      {
        return Math.min(num[start], num[end]);
      }

      int mid = start + (end - start) / 2;

      if (num[mid] < num[end])
      {
        return findMin(num, start, mid);
      }
      else
      {
        return findMin(num, mid + 1, mid);
      }
    }
  }

