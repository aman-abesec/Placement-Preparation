#========================================
#About Graph data structure
#========================================
#Directed Graph
    #Sum of indegrees=|E|
    #Sum of outdegree=|E|
    #Maximum number of edeges=|V|*(|V|-1)

#Undirected Graph
    #Sum of degrees=2*|E|
    #Maximum number of edeges=|V|*(|V|-1)/2

#========================================
#Graph Representation
#========================================
#Adjacency Matrix Representation
#Adjacency List Representation

#========================================
#Graph Adjacency List Representation
#========================================
#  0-1-3
#  \/
#  2

def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def printGraph(adj,v):
    for i in adj:
        for j in i:
            print(j,end=" ")
        print()
# adj=[[] for _ in range(4)]
# addedge(adj,0,1)
# addedge(adj,0,2)
# addedge(adj,1,2)
# addedge(adj,1,3)
# printGraph(adj,4)

#===========================================
#Comparison b/w adjacency list and Matrix
#===========================================
#adjacency list
    #Memory O(v+e)
    #any edge from u to v O(v)
    #all adjacency of u O(degree(u))
    #add an edge O(1)
    #Remove an edge O(v)
#adjacency Matrix
    #Memory O(v*v)
    #any edge from u to v O(1)
    #all adjacency of u O(v)
    #add an edge O(1)
    #Remove an edge O(1)

#============================================
#Breadth first Search(For Connected Graph)
#===========================================
from collections import deque
#BFS for Connected Graph
def bfs(adj,vertex,s):
    visited=[False for _ in range(vertex)]
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        u=q.popleft()
        print(u,end=" ")
        for v in adj[u]:
            if visited[v]==False:
                visited[v]=True
                q.append(v)

# 0 to (1,2)
# 1 to (0,3,2)
# 2 to (0,1,4)
# 3 to (1)
# 4 to (2)
# adj=[[] for i in range(5)]
# addedge(adj,0,1)
# addedge(adj,0,2)
# addedge(adj,2,1)
# addedge(adj,1,3)
# addedge(adj,2,3)
# addedge(adj,2,4)
# addedge(adj,3,4)
# bfs(adj,5,0)

#============================================
#Breadth first Search(For Dis-Connected Graph)
#===========================================
#T=O(v+e)
def bfs1(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        u=q.popleft()
        print(u,end=" ")
        for v in adj[u]:
            if visited[v]==False:
                visited[v]=True
                q.append(v)
def disConnectedGraph(adj,vertex):
    visited=[False for _ in range(vertex)]
    for i in range(vertex):
        if visited[i]==False:
            bfs1(adj,i,visited)
# adj=[[] for _ in range(7)]
# addedge(adj,0,1)
# addedge(adj,0,2)
# addedge(adj,1,3)
# addedge(adj,2,3)
# addedge(adj,4,5)
# addedge(adj,4,6)
# addedge(adj,5,6)
# disConnectedGraph(adj,7)

#============================================
#Count the number of disconnected Graph
#===========================================
#T=O(v+e)
def bfs1(adj,s,visited):
    q=deque()
    q.append(s)
    visited[s]=True
    while q:
        u=q.popleft()
        # print(u,end=" ")
        for v in adj[u]:
            if visited[v]==False:
                visited[v]=True
                q.append(v)
def disConnectedGraph(adj,vertex):
    count=0
    visited=[False for _ in range(vertex)]
    for i in range(vertex):
        if visited[i]==False:
            count+=1
            bfs1(adj,i,visited)
    return count
# adj=[[] for _ in range(7)]
# addedge(adj,0,1)
# addedge(adj,0,2)
# addedge(adj,1,3)
# addedge(adj,2,3)
# addedge(adj,4,5)
# addedge(adj,4,6)
# addedge(adj,5,6)
# print(disConnectedGraph(adj,7))

#============================================
#Deapth first Search(DFS for Connected Graph)
#===========================================
#T-O(v+e)
def dfsRec(adj,s,visited):
    visited[s]=True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u]==False:
            dfsRec(adj,u,visited)
# visited=[False for _ in range(7)]
# adj=[[1,4],[0,2],[1,3],[2],[0,5,6],[4,6],[4,5]]
# dfsRec(adj,0,visited)

#================================================
#Deapth first Search(DFS for Dis-Connected Graph)
#===================================================
#T-O(v+e)
def dfs1(adj,s,visited):
    visited[s]=True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u]==False:
            visited[u]=True
            dfs1(adj,u,visited)
def dfsDis(adj,vertex):
    visited=[False for _ in range(vertex)]
    for u in range(vertex):
        if visited[u]==False:
            dfs1(adj,u,visited)
            print()
# adj=[[1,2],[0,2],[0,1],[4],[3]]
# dfsDis(adj,5)

#================================================
#Shortest Path in an unweighted Graph
#===================================================
#T-O(v+e)
def ShortestPathUn(adj,s,vertex):
    visited=[False for _ in range(vertex)]
    distance=[-1 for _ in range(vertex)]
    distance[0]=0
    visited[0]=True
    q=deque()
    q.append(s)
    while q:
        u=q.popleft()
        for i in adj[u]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True
                distance[i]=distance[u]+1
    return distance
# adj=[[1,2],[0,3,2],[0,1,3],[1,2]]
# vertex=4
# print(ShortestPathUn(adj,0,vertex))

#===============================================
#Detect loop in Undirected Graph
#Using DFS
#===============================================
#T-O(v+e)
def isloopdfs(adj,s,visited,parent):
    visited[s]=True
    for v in adj[s]:
        if visited[v]==False:
            if isloopdfs(adj,v,visited,s)==True:
                return True
            elif parent!=v:
                return True
    return False

def isloopUn(adj,vertex):
    visited=[False for _ in range(vertex)]
    for i in range(vertex):
        if visited[i]==False:
            if isloopdfs(adj,i,visited,-1)==True:
                return True
    return False
# adj=[[1],[0,2,3],[1,3,4],[1,2],[2,5],[4]]
# print(isloopUn(adj,5))

#===============================================
#Detect loop in directed Graph Using Dfs
#===============================================
#T-O(v+e)
def isLoopDfs(adj,s,visited,rec):
    visited[s]=True
    rec[s]=True
    for v in adj[s]:
        if visited[v]==False and isLoopDfs(adj,v,visited,rec):
            return True
        elif rec[v]==True:
            return True
    rec[s]=False
    return False
def isloopD(adj,vertex):
    visited=[False for _ in range(vertex+1)]
    rec=[False for _ in range(vertex+1)]
    for i in range(vertex):
        if visited[i]==False:
            if isLoopDfs(adj,i,visited,rec)==True:
                return True
    return False

# adj=[[1],[],[1,3],[4],[5],[3]]
# vertex=5
# print(isloopD(adj,vertex))

#==================================================
#Topological Sorting (Kahn's Based Algorithm)
#BFS Based
#=================================================
#Note:>Valid for Acyclic Graph
#T-O(v+e)
from collections import deque
def topoSort(adj,vertex):
    #Store indegree of every vertex
    indegree=[0 for _ in range(vertex+1)]
    for u in adj:
        for v in u:
            indegree[v]+=1
    #Create a queue
    q=deque()
    #Add all 0 indegree vertices to the q
    for i in range(vertex):
        if indegree[i]==0:
            q.append(i)
    while q:
        u=q.popleft()
        print(u,end=" ")
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.append(v)
# vertex=4
# adj=[[2,3],[3,4],[3],[],[]]
# topoSort(adj,vertex)

#=====================================================
#Cycle Detection in Directed Graph using Kahn's algo
#Using BFS
#=======================================================
#T-O(v+e)
def detectCycle(adj,vertex):
    indegree=[0 for _ in range(vertex+1)]
    for u in adj:
        for v in u:
            indegree[v]+=1
    q=deque()
    for i in range(vertex):
        if indegree[i]==0:
            q.append(i)
    count=0
    while q:
        u=q.popleft()
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.append(v)
        count+=1
    return  vertex!=count

# adj=[[1],[2],[3],[1],[1]]
# vertex=4
# print(detectCycle(adj,vertex))

#========================================================
#Topological Sort using DFS
#======================================================
def topoDFS(adj,s,visited,stack):
    visited[s]=True
    for v in adj[s]:
        if visited[v]==False:
            topoDFS(adj,v,visited,stack)
    stack.append(s)

def toposortDFS(adj,vertex):
    visited=[False for _ in range(vertex+1)]
    stack=[]
    for u in range(vertex):
        if visited[u]==False:
            topoDFS(adj,u,visited,stack)
    while stack:
        print(stack.pop(),end=" ")

# adj=[[1],[3],[3,4],[4],[]]
# vertex=4
# toposortDFS(adj,vertex)

#========================================================
#Shortest Path in a Directed Acyclic Graph
#===============================================
import math
def shortestPathDAG(adj,vertex,weight):
    dist=[math.inf for _ in range(vertex+1)]
    dist[0]=0
    indegree=[0 for i in range(vertex+1)]
    for u in adj:
        for v in u:
            indegree[v]+=1
    q=deque()
    for i in range(vertex+1):
        if indegree[i]==0:
            q.append(i)
    topsort=[]
    while q:
        u=q.popleft()
        topsort.append(u)
        for i in adj[u]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for u in topsort:
        for v in adj[u]:
            if dist[v]>dist[u]+weight[f"{u}{v}"]:
                dist[v]=dist[u]+weight[f"{u}{v}"]
    print(dist)

adj=[[1],[2,3],[3],[]]
vertex=3
weight={"01":1,'12':3,"23":4,"13":2}
shortestPathDAG(adj,vertex,weight)
