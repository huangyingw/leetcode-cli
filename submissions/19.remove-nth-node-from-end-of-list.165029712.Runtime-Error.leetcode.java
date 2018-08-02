public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        ListNode fast = head;
        ListNode slow = head;

        while (n > 1)
        {
            fast = fast.next;
            n--;
        }

        if (fast == null)
        {
            return head.next;
        }

        fast = fast.next;

        while (fast.next != null)
        {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}