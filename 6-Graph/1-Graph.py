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
