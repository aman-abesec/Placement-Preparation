# Heap:
#     -left(i)=2*i+1
#     -right(i)=2*i+2
#     -parent(i)=abs(i-1/2)
import math
class minHeap:
    def __init__(self,cap):
        self.arr=[0 for _ in range(cap)]
        self.size=0
        self.cap=cap
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def insert(self,val):
        #T-O(log(n))
        if self.cap==self.size:return
        self.size+=1
        self.arr[self.size-1]=val
        i=self.size-1
        while i!=0 and self.arr[self.parent(i)]>self.arr[i]:
            self.arr[self.parent(i)],self.arr[i]= self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)
    def minHeapify(self,i):
        l=self.left(i)
        r=self.right(i)
        sm=i
        if l<self.size and self.arr[i]>self.arr[l]:
            sm=l
        if r<self.size and self.arr[sm]>self.arr[r]:
            sm=r
        if(i!=sm):
            self.arr[i],self.arr[sm]=self.arr[sm],self.arr[i]
            self.minHeapify(sm)
    def extractMin(self):
        if self.size==0:return math.inf
        if self.size==1:
            self.size-=1
            return self.arr[0]
        self.arr[0],self.arr[self.size-1]=self.arr[self.size-1],self.arr[0]
        self.size-=1
        self.minHeapify(0)
        return self.arr[self.size]
    def decreaseKey(self,i,key):
        #T-O(log(n))
        self.arr[i]=key
        while i!=0 and self.arr[i]<self.arr[self.parent(i)]:
            self.arr[i],self.arr[self.parent(i)]=self.arr[self.parent(i)],self.arr[i]
            i=self.parent(i)
    def deleteKey(self,i):
        self.decreaseKey(i,-math.inf)
        self.extractMin()
    def buildHeap(self):
        #T-O(log(n))
        for i in range((self.size-2)//2,-1,-1):
            self.minHeapify(i)
a=minHeap(10)
a.insert(200)
a.insert(70)
a.insert(10)
a.insert(100)
print(a.arr)
a.minHeapify(0)
print(a.arr)
print(a.extractMin())
a.deleteKey(1)
print(a.arr)
# print(a.arr)
