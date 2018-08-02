public class Solution
{
    public List<List<Integer>> pathSum(TreeNode root, int sum)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (root != null)
        {
            pathSum(root, sum, new ArrayList<Integer>(), result);
        }

        return result;
    }

    private void pathSum(TreeNode root, int sum, ArrayList<Integer> current,
                         List<List<Integer>> result)
    {
        if (root == null || root.val > sum)
        {
            return;
        }

        if (root.left == null && root.right == null)
        {
            if (root.val == sum)
            {
                ArrayList<Integer> temp = new ArrayList<Integer>(current);
                temp.add(root.val);
                result.add(temp);
            }

            return;
        }

        current.add(root.val);
        pathSum(root.left, sum - root.val, current, result);
        pathSum(root.right, sum - root.val, current, result);
        current.remove(current.size() - 1);
    }
}
