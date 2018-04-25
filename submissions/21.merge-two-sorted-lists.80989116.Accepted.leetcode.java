public class Solution
{
    public ListNode mergeTwoLists(ListNode p1, ListNode p2)
    {
        ListNode dummy = new ListNode(0);
        ListNode nav = dummy;

        while (p1 != null && p2 != null)
        {
            if (p1.val <= p2.val)
            {
                nav.next = p1;
                p1 = p1.next;
            }
            else
            {
                nav.next = p2;
                p2 = p2.next;
            }

            nav = nav.next;
        }

        nav.next = p1 != null ? p1 : p2;
        return dummy.next;
    }
}
