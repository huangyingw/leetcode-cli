public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        ListNode fast = head;
        ListNode slow = head;

        while (n > 0 && fast.next != null)
        {
            fast = fast.next;
            n--;
        }

        if (n > 0 && fast.next == null)
        {
            return head.next;
        }

        while (fast.next != null)
        {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}
