class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.binary_search(self.dictionary[key], timestamp)
        
    def binary_search(self, array, val):
        l = 0 
        r = len(array) - 1
        while l <= r:
            mid = (l + r) // 2
            if array[mid][0] <= val:
                l = mid + 1
            else:
                r = mid - 1
        return array[r][1] if r > -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)