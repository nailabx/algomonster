from utils.list_node import ListNode
from typing import Dict
from collections import defaultdict

class RemoveDupUnsortLinked:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        count = defaultdict(int) 
        cur = head  
        
        while cur:
            count[cur.val] += 1  # count each number
            cur = cur.next
        
        dummy = ListNode(0, head)   # dummy node that is before the head, pointing the head
        prev = dummy    # copy of dummy which we will use to connect the unique numbers
        
        while head:
            if count[head.val] > 1:  # then it is a duplicate
                prev.next = head.next   # skip the current head and point to the next one 
            else:
                prev = prev.next   # if it is unique, we can move on and include the node
            head = head.next
        
        return dummy.next 
