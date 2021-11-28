class SnapshotArray:

    # Define an array which stores pairs of the snapshot id and the value at that 
    # snapshot also store the current snapshot id
    def __init__(self, length: int):
        self.array = [[(-1, 0)] for _ in range(length)]
        self.cur_snap_id = 0

    # When we set a value add a new pair at that index to the array
    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.cur_snap_id, val))

    # Return the current snapshot id and increment the current snapshot id
    def snap(self) -> int:
        snap_id = self.cur_snap_id
        self.cur_snap_id += 1
        return snap_id

    # Binary search for the closest smaller snapshot id to the given snapshot id
    def get(self, index: int, snap_id: int) -> int:
        low = 0
        arr = self.array[index]
        high = len(arr)
        
        while low < high:
            mid = (low + high) // 2
            if arr[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid
        
        return self.array[index][high - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)