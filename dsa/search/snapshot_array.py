class SnapshotArray:

    def __init__(self, length: int):
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        # use binary search to find it
        l, r, pos = 0, len(self.histories[index]) - 1, -1
        while l <= r:
            mid = (r + l)//2
            if self.histories[index][mid][0] <= snap_id:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        return self.histories[index][pos][1]

