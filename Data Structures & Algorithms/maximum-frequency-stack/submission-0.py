from collections import Counter
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.counter = {}
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val,0)+1
        
        if self.freq[val] not in self.counter:
            self.counter[self.freq[val]] = []
        
        self.counter[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])
    def pop(self) -> int:
        ele = self.counter[self.maxFreq].pop()
        self.freq[ele] -= 1
        if not self.counter[self.maxFreq]:
            self.maxFreq -= 1
        return ele
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()