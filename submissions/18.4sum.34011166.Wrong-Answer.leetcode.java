public class Solution
{
    public List<List<Integer>> fourSum(int[] num, int target)
    {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        for (int i = 0; i < num.length - 3; i++)
        {
            if (i > 0 && num[i] == num[i - 1]) // avoid duplicate solutions
            {
                continue;
            }

            for (int j = i + 1; j < num.length - 2; j++)
            {
                if (j > i + 1 && num[j] == num[j - 1]) // avoid duplicate solutions
                {
                    continue;
                }

                int k = j + 1;
                int l = num.length - 1;

                while (k < l)
                {
                    int sum = num[i] + num[j] + num[k] + num[l];

                    if (sum > target)
                    {
                        l--;
                    }
                    else if (sum < target)
                    {
                        k++;
                    }
                    else if (sum == target)
                    {
                        ArrayList<Integer> temp = new ArrayList<Integer>();
                        temp.add(num[i]);
                        temp.add(num[j]);
                        temp.add(num[k]);
                        temp.add(num[l]);
                        result.add(temp);
                        k++;
                        l--;
                    }

                    while (k < l && l + 1 < num.length && num[l] == num[l + 1])
                    {
                        l--;
                    } // avoid duplicate solutions

                    while (k < l && k - 1 > i && num[k] == num[k - 1])
                    {
                        k++;
                    } // avoid duplicate solutions
                }
            }
        }

        return result;
    }
}

