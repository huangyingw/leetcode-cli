public class Solution
{
    private TreeNode sortedListToBST(ListNode head, int begin, int end)
    {
        if (begin > end)
        {
            return null;
        }

        TreeNode p = new TreeNode(0);
        int mid = begin + (end - begin) / 2;
        p.left = sortedListToBST(head, begin, mid - 1);
        p.val = head.val;
        head = head.next;
        p.right = sortedListToBST(head, mid + 1, end);
        return p;
    }

    public TreeNode sortedListToBST(ListNode head)
    {
        ListNode p = head;
        int len = 0;

        while (p != null)
        {
            len++;
            p = p.next;
        }

        return sortedListToBST(head, 0, len - 1);
    }
}
