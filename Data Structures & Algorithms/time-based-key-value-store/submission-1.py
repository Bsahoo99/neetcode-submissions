class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.storage:
            return ""

        record = self.storage[key]

        l = 0 
        r = len(record)

        while l < r:
            m = (l + r) // 2

            if record[m][1] <= timestamp:
                l = m + 1
            else:
                r = m 

        if l == 0:
            return ""

        return record[l - 1][0]
