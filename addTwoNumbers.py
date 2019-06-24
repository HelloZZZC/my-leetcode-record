"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
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

