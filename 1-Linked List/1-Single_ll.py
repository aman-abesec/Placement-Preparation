#===============================================
#          Implementation Of Singly Linked List
#==============================================
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

#===============================================
#      Traversal In Linked List
#==============================================

def traversal(curr):
    #Simple Traversal Of LinkedList
    while(curr!=None):
        print(curr.val,end=" ")
        curr=curr.next

def rectraversal(curr):
    #Recursive Traversal of LinkedList
    if curr==None:
        return
    print(curr.val,end=" ")
    rectraversal(curr.next)

#============================================
#     Insertion in Linked List
#===========================================

def insertatbeg(curr,data):
    #Insert at begin of LinkedList
    newNode=Node(data)
    if curr==None:
        return newNode
    newNode.next=curr
    return newNode

def insertatend(curr,data):
    #Insert at the end of LinkedList
    newNode=Node(data)
    temp=curr
    if temp==None:
        return newNode
    while temp.next!=None:
        temp=temp.next
    temp.next=newNode
    return curr

def insertatpos(curr,pos,data):
    #Insert at a given position
    newNode=Node(data)
    if pos==1:
        newNode.next=curr
        return newNode
    temp=curr
    for i in range(pos-2):
        temp=temp.next
        if temp==None:#Cornear Case
            return curr
    newNode.next=temp.next
    temp.next=newNode
    return curr

def sortedinsert(curr,data):
    #Insert in a Sorted Singly Linked List
    newNode=Node(data)
    if curr==None:
        return newNode
    temp=curr
    while True:
        if temp.val>=data:
            newNode.next=temp.next
            temp.next=newNode
            newNode.val,temp.val=temp.val,newNode.val
            return curr
        if temp.next==None:
            break
        temp=temp.next
    temp.next=newNod
    return curr

#============================================
#     Deletion in Linked List
#===========================================

def delatbeg(curr):
    #Delete at first Node
    if curr==None:
        return curr
    return curr.next

def delatlast(curr):
    #Delete at last Node
    temp=curr
    if curr==None:
        return curr
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return curr

def removeDuplicateSLL(curr):
    #Deleting Duplicate in Sorted LinkedList
    if curr==None or curr.next==None:
        return curr
    temp=curr
    while temp.next!=None and temp!=None:
        if temp.val==temp.next.val:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return curr

#============================================
#     Searching in Linked List
#===========================================

def itersearch(curr,data):
    #Searching by iterative Method
    while curr!=None:
        if curr.val==data:
            return True
        curr=curr.next
    return False

def recsearch(curr,data):
    #Searching by recursive Method
    if curr==None:
        return False
    if curr.val==data:
        return True
    return recsearch(curr.next,data)

def middleofll(curr):
    #Searching Middle element of a linked List
    if curr==None:
        return
    elif curr.next==None:
        return curr.val
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow.val

def nthNodefromend(curr,pos):
    #Searching nth Node from end of LinkedList
    if curr==None:return
    first=curr
    for i in range(pos):
        if first==None:return
        first=first.next
    second=curr
    while first!=None:
        second=second.next
        first=first.next
    return second.val

#=======================================
#      Reverse a singly LinkedList
#======================================

def revere(curr):
    #Reversing LinkedList Iterative Method
    if curr==None or curr.next==None:
        return curr
    pre=None
    temp=curr
    while curr!=None:
        temp=curr.next
        curr.next=pre
        pre=curr
        curr=temp
    return pre

def recReverse(curr,prev=None):
    #Reversing LinkedList by Recursive Method
    if curr==None:return prev
    temp=curr.next
    curr.next=prev
    return recReverse(temp,curr)


#Creating multiple Node
head=Node(9)
n1=Node(40)
n2=Node(40)
n3=Node(79)
head.next=n1
n1.next=n2
n2.next=n3
head=SegregateEvenOdd(head)
traversal(head)
