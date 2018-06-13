public class Solution
{
    public TreeNode buildTree(int[] inorder, int[] postorder)
    {
        HashMap inMap = new HashMap();

        for (int i = 0; i < inorder.length; i++)
        {
            inMap.put(inorder[i], i);
        }

        TreeNode root = helper(inMap, inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
        return root;
    }

    public TreeNode helper(HashMap inMap, int[] inorder, int inLeft, int inRight, int[] postorder, int poLeft, int poRight)
    {
        TreeNode root = new TreeNode(postorder[poRight]);
        int mid = (int)inMap.get(postorder[poRight]);
        root.left = helper(inMap, inorder, inLeft, mid - 1, postorder, poLeft, poLeft + mid - 1 - inLeft);
        root.right = helper(inMap, inorder, mid + 1, inRight, postorder, poRight - 1 - mid + 1 + inLeft, poRight - 1);
        return root;
    }
}
