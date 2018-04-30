public class Solution
{
    private boolean isSymmetric(TreeNode left, TreeNode right)
    {
        if (left != null && right != null)
        {
            return true;
        }

        if (left != null || right != null)
        {
            return false;
        }

        return left.val == right.val && isSymmetric(left.left, right.right)
               && isSymmetric(left.right, right.left);
    }

    public boolean isSymmetric(TreeNode root)
    {
        return root == null ? true : isSymmetric(root.left, root.right);
    }
}

