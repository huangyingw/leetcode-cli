public class Solution
{
    public List<Integer> rightSideView(TreeNode root)
    {
        List<Integer> ret = new ArrayList<Integer>();

        if (root == null)
        {
            return ret;
        }

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);

        while (!q.isEmpty())
        {
            int cnt = q.size();

            for (int i = 0; i < cnt; i++)
            {
                TreeNode cur = q.poll();

                if (i == cnt - 1)
                {
                    ret.add(cur.val);
                }

                if (cur.left != null)
                {
                    q.offer(cur.left);
                }

                if (cur.right != null)
                {
                    q.offer(cur.right);
                }
            }
        }

        return ret;
    }
}
