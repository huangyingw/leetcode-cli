class Solution(object):
    def reverseList(self, head):
        if not head:
            return head

        pre = None

        while head.next:
            temp = head.next
            head.next = pre
            pre = head
            head = temp

        return pre