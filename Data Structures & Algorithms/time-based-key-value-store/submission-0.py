class TimeMap:

    def __init__(self):
        self.keystore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # iterate the list for that key and get the value which has that timestamp
        seen = 0
        values = self.keystore.get(key, [])
        for i in range(len(values)):
            if values[i][1] <= timestamp:
                seen = max(seen, values[i][1])
        for i in range(len(values)):
            if values[i][1] == seen:
                return values[i][0]
        return ""
        
