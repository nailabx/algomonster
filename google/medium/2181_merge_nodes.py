from typing import Optional
from utils.list_node import ListNode

class MergeNodes:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res: ListNode = ListNode()
        tmp: ListNode = res
        while head:
            curr = head.next
            merge: int = 0
            while curr and curr.val != 0:
                merge += curr.val
                curr = curr.next
            if merge > 0:
                tmp.next = ListNode(merge)
                tmp = tmp.next
            head = curr
        return res.next