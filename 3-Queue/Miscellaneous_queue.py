#================================================
#Implementation Of Stack using Queue
#================================================
class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
    def top(self):
        return self.q1.getfront()
    def size(self):
        return self.q1.length()
    def pop(self):
        d=self.q1.getfront()
        self.q1.deque()
        return d
    def push(self,data):
        while self.q1.empty()==False:
            self.q2.enque(self.q1.getfront())
            self.q1.deque()
        self.q1.enque(data)
        while self.q2.empty()==False:
            self.q1.enque(self.q2.getfront())
            self.q2.deque()
s=Stack()
s.push(90)
s.push(100)
print(s.pop())
# print(s.top())
