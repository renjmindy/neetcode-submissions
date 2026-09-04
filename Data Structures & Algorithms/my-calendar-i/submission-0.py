class MyCalendar:
    
    def __init__(self):
        self.mp = list()

    def book(self, startTime: int, endTime: int) -> bool:
        for ini, end in self.mp:
            if not (ini >= endTime or end <= startTime): return False
        
        self.mp.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)