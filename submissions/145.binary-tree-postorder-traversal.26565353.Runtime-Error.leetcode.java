public class Solution
{
    public List<Integer> postorderTraversal(TreeNode root)
    {
        List<Integer> result = new ArrayList<Integer>();
        helper(root, result);
        return result;
    }
    public void helper(TreeNode root, List<Integer> result)
    {
        helper(root.left, result);
        helper(root.right, result);
        result.add(root.val);
    }
}
