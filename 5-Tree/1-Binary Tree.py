#=============================================
#Implementation of Binary Tree
#============================================
class Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

#===============================================
#Implementation Of preordertraversal Recursively
#===============================================
#T=O(n)
#S=O(n)
def pretraversalRec(head):
    if head==None:
        return
    print(head.val,end=" ")
    pretraversalRec(head.left)
    pretraversalRec(head.right)

#===============================================
#Implementation Of inordertraversal Recursively
#===============================================
#T=O(n)
#S=O(n)
def intraversalRec(head):
    if head==None:
        return
    intraversalRec(head.left)
    print(head.val,end=" ")
    intraversalRec(head.right)

#===============================================
#Implementation Of postordertraversal Recursively
#===============================================
#T=O(n)
#S=O(n)
def posttraversalRec(head):
    if head==None:
        return
    posttraversalRec(head.left)
    posttraversalRec(head.right)
    print(head.val,end=" ")

#===============================================
#Height of a binary Tree
#===============================================
#T=O(n)
#S=O(n)
def height(head):
    if head==None:
        return 0
    return 1+max(height(head.left),height(head.right))

#===============================================
#Print Node at K Distnce
#===============================================
#T=O(n)
#S=O(h)
def printNodeK(head,pos):
    if head==None:return
    if pos==0:
        print(head.val,end=' ')
    else:
        printNodeK(head.left,pos-1)
        printNodeK(head.right,pos-1)

#===============================================
#Level Order Traversal
#===============================================
#T=O(n)
#S=O(n)
def levelorder(head):
    if head==None:return
    queue=[head]
    while queue!=[]:
        t=queue.pop(0)
        print(t.val,end=" ")
        if t.left!=None:
            queue.append(t.left)
        if t.right!=None:
            queue.append(t.right)

#===============================================
#Level Order Traversal Line By Line
#===============================================
#T-O(n)
#S-O(n)
             #Method-1
def levelorderLinebyLine(head):
    queue=[]
    queue.append(head)
    queue.append(None)
    while len(queue)>1:
        t=queue.pop(0)
        if t==None:
            queue.append(None)
            print()
            continue
        print(t.val,end=" ")
        if t.left!=None:queue.append(t.left)
        if t.right!=None:queue.append(t.right)

            #Method-2
#T=O(n)
#S=O(width of tree)
def levelorderLinebyLine2(head):
    if head==None:return
    queue=[]
    queue.append(head)
    while len(queue)>0:
        s=len(queue)
        for i in range(s):
            t=queue.pop(0)
            print(t.val,end=" ")
            if t.left!=None:queue.append(t.left)
            if t.right!=None:queue.append(t.right)
        print()

#============================================
#Size of a Binary Tree
#============================================
#T=O(n)
#S=O(h)
def sizeoftree(head):
    if head==None:return 0
    return 1+sizeoftree(head.left)+sizeoftree(head.right)

#============================================
#Maximum in a Binary Tree
#============================================
#T-O(n)
#T-S(h)
import math
def maxinbinarytree(head):
    if head==None:return -math.inf
    return max(head.val,max(maxinbinarytree(head.left),maxinbinarytree(head.right)))

#============================================
#Print Left View of Binary Tree
#============================================
#==================Recursive Solution=====
#T-O(n)
#T-S(h)
maxlevel=0
def leftviewrec(head,level=1):
    global maxlevel
    if head==None:return
    if maxlevel<level:
        print(head.val)
        maxlevel=level
    leftviewrec(head.left,level+1)
    leftviewrec(head.right,level+1)

#==================Iterative Solution=====
#T-O(n)
#T-S(w)
def leftviewiter(head):
    if head==None:return
    queue=[]
    queue.append(head)
    while queue!=[]:
        c=len(queue)
        for i in range(c):
            temp=queue.pop(0)
            if i==0:
                print(temp.val)
            if temp.left!=None:queue.append(temp.left)
            if temp.right!=None:queue.append(temp.right)

#============================================
#Children Sum Property
#============================================
#T-O(n)
#T-S(w)
def csp(head):
    if head==None:return True
    if head.left==None and head.right==None:return True
    sm=0
    if head.left!=None:sm+=head.left.val
    if head.right!=None:sm+=head.right.val
    return (head.val==sm and csp(head.left) and csp(head.right))

#============================================
#Check for balanced Tree
#============================================
#===============Method-1============
#T-O(n^2)
#T-S(w)
def isbalanced1(head):
    if head==None:return True
    hl=height(head.left)
    hr=height(head.right)
    return abs(hl-hr)<=1 and isbalanced(head.left) and isbalanced(head.right)

#==============Method-2=========
#T-O(n)
#T-S(h)
def isbalanced2(head):
    if head==None:return 0;
    lh=isbalanced2(head.left)
    if lh==-1:return -1
    rh=isbalanced2(head.right)
    if rh==-1:return -1
    if(abs(lh-rh)>1):
        return -1
    else:
        return max(lh,rh)+1

#===========================================
#Maximum width of a binary tree
#============================================
#T-O(n)
#T-S(max width)
def maxwidth(head):
    if head==None:return 0;
    queue=[]
    queue.append(head)
    queue.append(None)
    mx=0
    while len(queue)>1:
        c=0
        while queue[0]!=None:
            s=queue.pop(0)
            if s.left!=None:queue.append(s.left)
            if s.right!=None:queue.append(s.right)
            c+=1
        mx=max(mx,c)
        queue.append(queue.pop(0))
    return mx

#===========================================
#Convert Binary tree to doubly linked List
#============================================
#T-O(n)
#T-S(h)
prev=None
def btodll(head):
    if head==None:return head
    root=btodll(head.left)
    if prev==None:
        root=head
    else:
        head.left=prev
        prev.right=head
    prev=head
    btodll(head.right)
    return root

#===========================================
#Construct a binary tree from in and pre order
#============================================
#Note Using hashing we can reduce the time complexcity O(n)
#T-O(n^2)
preIndex=0
def ConstructTree(inList,preList,s,e):
    if s>e:return None
    global preIndex
    p=preIndex
    root=Tree(preList[p])
    preIndex+=1
    for i in  range(s,e+1):
        if inList[i]==root.val:
            inIndex=i
            break
    root.left=ConstructTree(inList,preList,s,inIndex-1)
    root.right=ConstructTree(inList,preList,inIndex+1,e)
    return root

#===========================================
#Tree Traversal in Spiral Form
#============================================
# Note :This Question also can be solve using
# two stack(Most optimize)
#T-O(n)
#T-S(h)
def printSpiralform(head):
    if head==None:return
    queue=[]
    stack=[]
    flag=False
    queue.append(head)
    while queue!=[]:
        count=len(queue)
        for i in range(count):
            curr=queue[0]
            queue.pop(0)
            if flag:
                stack.append(curr.val)
            else:
                print(curr.val,end=" ")
            if curr.left!=None:queue.append(curr.left)
            if curr.right!=None:queue.append(curr.right)
        if flag:
            while stack!=[]:
                print(stack[-1],end=" ")
                stack.pop()
        flag=~flag
        print()

#===========================================
#Diameter of Binary Tree
#============================================
#T-O(n^2)
#T-S(h)
def Diameter(head):
    # Method1
    if head==None:return 0
    mx=1+height(head.left)+height(head.right)
    l=Diameter(head.left)
    r=Diameter(head.right)
    return max(l,r,mx)

res=0
#T-O(n)
#T-S(h)
def Diameter2(head):
    # Method2
    global res
    if head==None:return 0
    l=Diameter2(head.left)
    r=Diameter2(head.right)
    res=max(res,(1+l+r))
    return 1+max(l,r)

#===========================================
#LCA of binary Tree
#============================================
#Method-1
#T-O(n)
#T-S(n)
def finPath(head,arr,ele):
    if head==None: return False
    arr.append(head)
    if head.val==ele:return True
    if finPath(head.left,arr,ele) or finPath(head.right,arr,ele):
        return True
    arr.pop()
    return False

def lca(head,n1,n2):
    arr1=[]
    arr2=[]
    if(finPath(head,arr1,n1)==False or finPath(head,arr2,n2)==False):
        return None
    i=0
    while i<len(arr1) and i<len(arr2):
        if arr1[i+1]!=arr2[i+1]:
            return arr1[i]
        i+=1
    return False

#The below functrion only work when both node present in the tree
#T-O(n)
#T-S(h)
def lca2(head,n1,n2):
    if head==None:return None
    if head.val==n1 or head.val==n2:return head
    l=lca2(head.left,n1,n2)
    r=lca2(head.right,n1,n2)
    if l!=None  and r!=None:return head
    if l!=None:return l
    if r!=None:return r

#===========================================
#Burn a Binary Tree From a Leaf
#============================================
#T-O(n)
#T-S(n)
#Note:Just we have to find the fasthest Node


#===========================================
#Inoreder Iterative Traversal
#============================================
#T-O(n)
#T-S(n)
def inorderIter(root):
    stack=[]
    curr=root
    while curr!=None or stack!=[]:
        while curr!=None:
            stack.append(curr)
            curr=curr.left
        curr=stack.pop()
        print(curr.val,end=" ")
        curr=curr.right
        
#===========================================
#Preorder Iterative Traversal
#============================================
#T-O(n)
#T-S(n)
def preorIter(root):
    stack=[]
    curr=root
    while curr!=None or stack!=[]:
        while curr!=None:
            stack.append(curr)
            print(curr.val,end=" ")
            curr=curr.left
        curr=stack.pop()
        curr=curr.right
        
parent=Tree(50)
parent.left=Tree(40)
parent.right=Tree(30)
parent.left.left=Tree(70)
parent.left.right=Tree(60)
parent.right.left=Tree(80)
parent.right.right=Tree(90)
parent.right.right.left=Tree(190)
parent.right.right.right=Tree(200)
