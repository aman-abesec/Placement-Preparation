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

#=============================================
# Infix to Postfix Conversion
#==============================================
def intopost(s):
    #1-Create an empty stack
    stack=[]
    #2-Traverse for each character in string
    for i in s:
        #3-If i is operand print it
        if i not in ['^','*','/','+','-','(',')']:
            print(i,end="")
        else:
            #4-If i is left parenthesis push it in stack
            if i=='(':
                stack.append('(')
            #5-If i is Operator the check stack is empty then push it otherwise check precedence if high the push in stack otherwise
            #pop untill less precedence find
            elif i!=')':
                priority={'^':5,'*':4,'/':3,'+':2,'-':1}
                if stack==[] or stack[-1]=='(' or priority[i]>=priority[stack[-1]]:
                    stack.append(i)
                elif stack!=[]:
                    while stack!=[] and priority[i]<=priority[stack[-1]]:
                        print(stack.pop(),end="")
                    stack.append(i)
            #6-If Right Parenthesis pop untill Left parenthesis Found
            else:
                while stack!=[] and stack[-1]!='(':
                    print(stack.pop(),end="")
                stack.pop()
    #7-Pop the stack
    while stack!=[]:
        print(stack.pop(),end="")
#intopost('(a+b)*(c+d)')


#=============================================
# Evaluation of Postfix Expression
#==============================================
def evalpostfix(s):
    #1-Create an empty stack
    stack=[]
    #2-Traverse through the every symbol
    for i in s:
        #3-if i is operand push in stack
        if i not in ('+','-','*','/'):
            stack.append(i)
        #4-if i is operation pop two values
        else:
            v1=stack.pop()
            v2=stack.pop()
            #5-append in stack (v2+i+v1)
            stack.append(f'({v2}{i}{v1})')
    #6- return stack top
    return stack[-1]
#print(evalpostfix('ab*cd*+e-'))

#=============================================
# Infix to Prefix
#==============================================
def intopre(s):
    #1-Create an empty Stack
    stack=[]
    #2-Create an empty string
    ans=""
    #3-Revere the string
    s=s[::-1]
    #4-Travere the revere string
    for i in s:
        #5-If i is operand append it in empty string
        if i not in ['^','*','/','+','-','(',')']:
            ans+=i
        else:
            #6-If left parenthesis append to Stack
            if i==')':
                stack.append(i)
            #7-If Left parenthesis pop untill left parenthesis not found
            elif i=='(':
                while stack!=[] and stack[-1]!=')':
                    ans+=stack.pop()
                stack.pop()
            #8-If i is Operator
            else:
                priority={'^':5,'*':4,'/':3,'+':2,'-':1}
                #9-If stack is empty then push
                if stack==[]:
                    stack.append(i)
                else:
                    #10-If priority of top is high then pop untill lower found else append in stack
                    if priority[i]<priority[stack[-1]]:
                        while stack!=[] and priority[i]<priority[stack[-1]]:
                            ans+=stack.pop()
                        stack.append(i)
                    else:
                        stack.append(i)
    #11-Add in string untill stack is not empty
    while stack!=[]:
        ans+=stack.pop()
    #12-Return Revere of the empty string
    return ans[::-1]
# print(intopre("x+y*z"))

#=============================================
# Evaluation of Postfix
#==============================================
def evalpost(s):
    stack=[]
    for i in s:
        if i in ['^','*','/','+','-']:
            v1=stack.pop()
            v2=stack.pop()
            stack.append(f'({v2}{i}{v1})')
        else:
            stack.append(i)
    return stack[-1]
#print(evalpost("acb+*"))

#==========================================
# Evaluation of Prefix
#============================================
def evalpre(s):
    stack=[]
    s=s[::-1]
    for i in s:
        if i in ['^','*','/','+','-']:
            v1=stack.pop()
            v2=stack.pop()
            stack.append(f'({v2}{i}{v1})')
        else:
            stack.append(i)
    return stack[-1]
#print(evalpre('+*abc'))

#==========================================
#Previous Greatest Element
#==========================================
def preGreatest(num):
    stack=[]
    ans=[]
    stack.append(num[0])
    ans.append(-1)
    for i in range(1,len(num)):
        while stack!=[] and stack[-1]<=num[i]:
            stack.pop()

        if stack==[]:
            ans.append(-1)
            stack.append(num[i])
        else:
            ans.append(stack[-1])
            stack.append(num[i])
    return ans
# print(preGreatest([15,10,18,12,4,6,2,8]))
# print(preGreatest([8,10,12]))
# print(preGreatest([12,10,8,8]))

#==========================================
#Next Greatest Element
#==========================================
def nextGreatest(num):
    stack=[]
    ans=[]
    stack.append(num[-1])
    ans.append(-1)
    for i in range(len(num)-2,-1,-1):
        while stack!=[] and stack[-1]<=num[i]:
            stack.pop()

        if stack==[]:
            ans.append(-1)
            stack.append(num[i])
        else:
            ans.append(stack[-1])
            stack.append(num[i])
    return ans[::-1]
# print(nextGreatest([5,15,10,8,6,12,9,18]))
# print(nextGreatest([10,15,20,25]))
# print(nextGreatest([25,20,15,10]))

#==========================================
#Previous Smallest Element
#==========================================
def prevSmallest(num):
    stack=[0]
    ans=[-1]
    for i in range(1,len(num)):
        while stack!=[] and  num[stack[-1]]>=num[i]:
            stack.pop()
        if stack==[]:
            ans.append(-1)
            stack.append(i)
        else:
            ans.append(stack[-1])
            stack.append(i)
    return ans
# print(prevSmallest([6,2,5,4,1,5,6]))

#==========================================
#Next Smallest Element
#==========================================
def nextSmallest(num):
    stack=[len(num)-1]
    ans=[len(num)]
    for i in range(len(num)-2,-1,-1):
        while stack!=[] and num[stack[-1]]>=num[i]:
            stack.pop()
        if stack==[]:
            ans.append(len(num))
            stack.append(i)
        else:
            ans.append(stack[-1])
            stack.append(i)
    return ans[::-1]
# print(nextSmallest([6,2,5,4,1,5,6]))

#=============================================
#Largest Rectangular Area in a Histogram
#=============================================
def larAreaHisto(num):
    ps=prevSmallest(num)
    ns=nextSmallest(num)
    # print(ps,ns)
    ans=0
    for i in range(len(num)):
        ans=max(ans,(ns[i]-ps[i]-1)*num[i])
    return ans
# print(larAreaHisto([4,2,1,5,6,3,2,4,2]))
# larAreaHisto([6,2,5,4,1,5,6])

#=============================================
#Largest Rectangle with 1' matrix
#Time Complacity O(m*n)
#=============================================
def larRectmat(mat):
    mx=larAreaHisto(mat[0])
    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=0:
                mat[i][j]+=mat[i-1][j]
        mx=max(mx,larAreaHisto(mat[i]))
    return mx
# print(larRectmat([[1,0,0,1,1],
#             [0,0,0,1,1],
#             [1,1,1,1,1],
#             [0,1,1,1,1]]))
