class TimeMap:

    def __init__(self):
        self.time = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.time:
            return ""
        arr = self.time[key]
        for t, v in arr:
            if t <= timestamp:
                res = v
            else:
                break
        
        return res