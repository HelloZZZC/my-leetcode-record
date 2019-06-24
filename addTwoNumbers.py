# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        diff = 0
        while l1 or l2 or diff:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            sum = l1_num + l2_num + diff
            node = ListNode(sum % 10)
            if head is None:
                head = node
            else:
                head = self.append(head, node)
            diff = 0 if sum / 10 < 1 else int(sum / 10)
            l1 = None if not l1 or l1.next is None else l1.next
            l2 = None if not l2 or l2.next is None else l2.next
        result = []
        data = head
        while data.next:
            result.append(data.val)
            data = data.next
        result.append(data.val)
        return result

    def append(self, head, node):
        end_node = head
        while end_node.next:
            end_node = end_node.next
        end_node.next = node
        return head


if __name__ == '__main__':
    node = ListNode(2)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node1.next = node2
    node.next = node1
    node3 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(4)
    node4.next = node5
    node3.next = node4
    obj = Solution()
    result = obj.addTwoNumbers(node, node3)

