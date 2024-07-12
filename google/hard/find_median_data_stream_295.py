from typing import List
import heapq

class FindMediamDataStream:
    def __init__(self):
        self.left_heap: List[int] = [] #min heap
        self.right_heap: List[int] = [] #max heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right_heap, -1 * num)
        heapq.heappush(self.left_heap, -1 * heapq.heappop(self.right_heap))
        if len(self.left_heap) > len(self.right_heap):
            heapq.heappush(self.right_heap, -1 * heapq.heappop(self.left_heap))
        print(self.left_heap)
        print(self.right_heap)
        
        

    def findMedian(self) -> float:
        l_n: int = len(self.left_heap)
        r_n: int = len(self.right_heap)
        if l_n == r_n:
            return (self.left_heap[0] - self.right_heap[0])/2
        return -self.right_heap[0]