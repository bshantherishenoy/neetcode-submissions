class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.size = 0
        self.front = 0
        self.rear = -1
             

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else: 
            self.rear = (self.rear + 1)% self.capacity
            self.q[self.rear] = value
            self.size +=1
            return True 


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True 
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True 
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True 
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()