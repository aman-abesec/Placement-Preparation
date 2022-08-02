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
adj=[[] for _ in range(4)]
addedge(adj,0,1)
addedge(adj,0,2)
addedge(adj,1,2)
addedge(adj,1,3)
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
