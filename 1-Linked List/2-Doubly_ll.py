#==================================================
#      Implementation of Doubly Linked List
#================================================
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None

#===============================================
#      Traversal In Doubly Linked List
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
#     Insertion in Doubly Linked List
#===========================================

def insertatbeg(curr,data):
    #Insert at begin of Doubly LinkedList
    newNode=Node(data)
    if curr==None:
        return newNode
    newNode.next=curr
    curr.prev=newNode
    return newNode

def insertatend(curr,data):
    #Insert at the end of Doubly LinkedList
    newNode=Node(data)
    temp=curr
    if temp==None:
        return newNode
    while temp.next!=None:
        temp=temp.next
    newNode.prev=temp
    temp.next=newNode
    return curr

#============================================
#     Deletion in Doubly Linked List
#===========================================

def delatbeg(curr):
    #Delete at first Node
    if curr==None or curr.next==None:
        return None
    curr=curr.next
    curr.prev=None
    return curr

def delatlast(curr):
    #Delete at last Node
    temp=curr
    if curr==None or curr.next==None:
        return curr
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return curr

#============================================
#     Reverse in Doubly Linked List
#===========================================

def reverse(curr):
    #Reversing by iterative Method
    if curr==None or curr.next==None:
        return curr
    pre=None
    temp=curr
    while temp!=None:
        temp.next,temp.prev=temp.prev,temp.next
        pre=temp
        temp=temp.prev
    return pre

#===Initilization of Doubly Linked LinkedList
head=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
head.next=n1
n1.prev=head
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
head=reverse(head)
traversal(head)
