/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public TreeNode sortedArrayToBST(int[] num)
    {
        if (num == null || num.length == 0)
        {
            return null;
        }

        return helper(num, 0, num.length - 1);
    }
    public TreeNode helper(int [] num, int l, int r)
    {
        if (l < r || l < 0 || r < 0)
        {
            return null;
        }

        int m = (l + r) / 2;
        TreeNode root = new TreeNode(num[m]);
        root.left = helper(num, l, m - 1);
        root.right = helper(num, m + 1, r);
        return root;
    }
}
