#====================================================
#            Queue implementation Using Linkedlist
#====================================================
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.cap=0
    def enque(self,data):
        newNode=Node(data)
        if self.cap==0:
            self.front=newNode
        else:
            self.rear.next=newNode
        self.rear=newNode
        self.cap+=1
    def deque(self):
        if self.front==None:
            return math.inf
        else:
            data=self.front.val
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.cap-=1
            return  data
    def length(self):
        return self.cap
    def isempty(self):
        return self.cap==0
    def getfront(self):
        return self.front.val
    def getrear(self):
        return self.rear.val
q=Queue()
q.enque(30)
q.enque(50)
print(q.deque())
print(q.getfront(),q.getrear(),q.length())
