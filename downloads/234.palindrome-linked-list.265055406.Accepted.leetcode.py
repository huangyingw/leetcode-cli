class Solution:
    def isPalindrome(self, head):
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        l = len(temp_list)
        for i in range(0, l // 2):
            if temp_list[i] != temp_list[l - 1 - i]:
                return False
        return True

    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

