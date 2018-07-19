public class Solution
{
    public ListNode swapPairs(ListNode head)
    {
        ListNode first = head;
        ListNode pre = null;

        while (first != null && first.next != null)
        {
            ListNode second = first.next;

            if (pre == null)
            {
                head = second;
            }

            pre = first;
            first.next = second.next.next;
            second.next = first;
            first = first.next;
        }

        return head;
    }
}
