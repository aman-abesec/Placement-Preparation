#============================================
#    Sorted Insert in a Singly LinkedList
#=============================================
def sortedinsert(curr,data):
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
    temp.next=newNode
    return curr

#============================================
#          Middle of a LinkedList
#=============================================
def middleofll(curr):
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

#============================================
#          Nth Node From End of a LinkedList
# T-O(n)
# s-O(1)
#=============================================
def nthNodefromend(curr,pos):
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

#==================================================
#          Remove Duplicate in Sorted LinkedList
#===================================================
def removeDuplicateSLL(curr):
    if curr==None or curr.next==None:
        return curr
    temp=curr
    while temp.next!=None and temp!=None:
        if temp.val==temp.next.val:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return curr

#=======================================================
#      Detect Loop in LinkedList(Floyd Cycle Detection)
#==========================================================
def isloop(curr):
    #Complacity O(length of linked list)
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:return True
    return False

#==========================================================
#             Remove loop of a linked list
#===========================================================
def removeloop(curr):
    fast=curr
    slow=curr
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
    if fast!=slow:return curr
    fast=curr
    while fast.next!=slow.next:
        fast=fast.next
        slow=slow.next
    slow.next=None
    return curr

#========================================================
#     Segregate Even odd nodes
#========================================================
def SegregateEvenOdd(curr):
    if curr==None:
        return curr
    estart,eend=None,None
    ostart,oend=None,None
    temp=curr
    while temp!=None:
        if temp.val%2==0:
            if estart==None:
                estart=temp
                eend=temp
            else:
                eend.next=temp
                eend=temp
        else:
            if ostart==None:
                ostart=temp
                oend=temp
            else:
                oend.next=temp
                oend=temp
        temp=temp.next
    if estart==None:return ostart
    elif ostart==None:return estart
    else:
        eend.next=ostart
        oend.next=None
        return estart

#===================================================
#       Intersection of two Linked List
#====================================================
def intersection(curr1,curr2):
    c1,c2=0,0
    temp1,temp2=curr1,curr2
    while temp1!=None:
        temp1=temp1.next
        c1+=1
    while temp2!=None:
        temp2=temp2.next
        c2+=1
    diff=abs(c1-c2)
    if c1>=c2:
        for i in range(diff):
            curr1=curr1.next
    else:
        for i in range(diff):
            curr1=curr1.next
    while curr1!=curr2:
        curr1=curr1.next
        curr2=curr2.next
    print(curr1.val)

#=================================================
#   Merge Two Sorted LinkedList
#==============================================
def mergeSorted(list1,list2):
    if list1==None:
        return list2
    if list2==None:
        return list1
    head,ptr=None,None
    while list1!=None and list2!=None:
        if(list1.val>=list2.val):
            if(head==None):
                head=list2
                ptr=list2
            else:
                ptr.next=list2
                ptr=list2
            list2=list2.next
        else:
            if(head==None):
                head=list1
                ptr=list1
            else:
                ptr.next=list1
                ptr=list1
            list1=list1.next
    if(list1==None):
        ptr.next=list2
    else:
        ptr.next=list1
    return head
