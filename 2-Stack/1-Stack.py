#==============================================
#            Stack implementation
#============================================
import math
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        self.size+=1
    def pop(self):
        if self.size==0:
            print("Under Flow")
            return math.inf
        value=self.head.val
        self.head=self.head.next
        self.size-=1
        return value
    def peek(self):
        if self.head==None:
            return -math.inf
        return self.head.val
    def length(self):
        return self.size
    def show(self):
        temp=self.head
        while temp!=None:
            print(temp.val,end=" ")
            temp=temp.next

#=========================================
# Check for balanced Parenthesis
#==========================================

def isBalancedParenthesis(parenthesis):
    stack=Stack()
    for i in parenthesis:
        if i=='(' or i=='{' or i=='[':
            stack.push(i)
        else:
            if stack.length()==0:
                return False
            else:
                bracket_dict={')':'(','}':'{',']':'['}
                if stack.peek()==bracket_dict[i]:
                    stack.pop()
                else:
                    return False
    if stack.length()==0:
        return True
    return False

#=================Implementation Stack============
s1=Stack()
s1.push(40)
s1.push(30)
s1.push(20)
s1.push(10)
s1.show()
print(s1.length())
s1.pop()
s1.show()
print(isBalancedParenthesis("({})[({(())})]"))
