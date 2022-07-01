#======================================================
#         Implementation of Single Circular LinkedList
#=======================================================
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

#=====================================
# Traversal of Circular linked list
#===================================
def traversal(curr):
    #Iterative traveral
    if curr==None:
        return
    temp=curr.next
    print(curr.val,end=" ")
    while curr!=temp:
        print(temp.val,end=" ")
        temp=temp.next

#=========================================
#    Insertion in Circular Linked List
#=========================================
def insertatbeg(curr,data):
    #Insert at beginning
    newNode=Node(data)
    if curr==None:
        newNode.next=newNode
        return newNode
    newNode.next=curr.next
    curr.next=newNode
    newNode.val,curr.val=curr.val,newNode.val
    return curr

def insertatend(curr,data):
    #Insert at End
    newNode=Node(data)
    if curr==None:
        newNode.next=newNode
        return newNode
    newNode.next=curr.next
    curr.next=newNode
    newNode.val,curr.val=curr.val,newNode.val
    return curr.next

#=========================================
#    Deletion in a Circular LinkedList
#==========================================
def delatbeg(curr):
    #Delete First Node
    if curr==None or curr==curr.next:
        return None
    curr.val=curr.next.val
    curr.next=curr.next.next
    return curr

def delatend(curr):
    #Delete Last node of Circular LinkedList
    if curr==None or curr==curr.next:
        return None
    temp=curr
    while temp.next.next!=curr:
        temp=temp.next
    temp.next=temp.next.next
    return curr

def deletekthnode(curr,pos):
    #Deletion at a given Position
    if curr==None:
        return None
    temp=curr
    if pos==1:
        if temp.next==temp:
            return None
        temp.val=temp.next.val
        temp.next=temp.next.next
        return curr
    for i in range(pos-2):
        temp=temp.next
    temp.next=temp.next.next
    return curr

#======================================================
#         Implementation of Doubly Circular LinkedList
#=======================================================
class DNode:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

#Implementation of Doubly Circular Linked List
head=DNode(10)
n1=DNode(20)
n2=DNode(30)
n3=DNode(40)
head.next=n1
n1.prev=head
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=head

#Implementing Circular LinkedList
# head=Node(10)
# n1=Node(20)
# n2=Node(30)
# n3=Node(40)
# head.next=n1
# n1.next=n2
# n2.next=n3
# n3.next=head
