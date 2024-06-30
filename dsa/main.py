from algomonster.dsa.search.snapshot_array import SnapshotArray
if __name__ == "__main__":
    s = SnapshotArray(3)
    s.set(0, 5)
    s.snap()
    s.set(0, 6)
    print(s.get(0, 0))