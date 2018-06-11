/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution 
{
    public boolean isSameTree(TreeNode p, TreeNode q) 
    {
        if(null == p || null == q)
        {
            return q == p;
        }
        
        if(p.val != q.val)
        {
            return false;
        }
        
        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
}
