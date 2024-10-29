class Graph:
    def __init__(self):
        self.node_count=0
        self.visited=[]
        self.graph={}
    def add_node(self,v):
        if v in self.graph:
            print(v," is Already present")
        else:
            self.graph[v]=[]
    def add_edge(self,v1,v2):
        if v1 not in self.graph:
            print(v1,"Not present")
        elif v2 not in self.graph:
            print(v2,"Not present")
        else:
            # lnist1=[v2]
            # list2=[v1,cost]
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
    def delNode(self,v):
        if v not in self.graph:
            print(v," Not Present")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1=self.graph[i]
                if v in list1:
                    list1.remove(v)

    def DFS(self,v):
        if v not in self.graph:
            print(v," Not in the graph")
            return
        if v not in self.visited:
            print(v,end=" ")
            self.visited.append(v)
            for i in self.graph[v]:
                self.DFS(i)

    def BFS(self,v):
        if v not in self.graph:
            print("Node is not present ")
            return
        queue=[]
        visited=[]
        queue.append(v)
        visited.append(v)
        while queue:
            current=queue.pop(0)
            print(current,end=" ")
            for i in self.graph[current]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)


g1=Graph()
g1.add_node('A')
g1.add_node('B')
g1.add_node('C')
g1.add_node('D')
g1.add_node('E')
g1.add_node('F')
g1.add_node('K')
g1.add_edge('A','B')
g1.add_edge('A','C')
g1.add_edge('B','D')
g1.add_edge('B','E')
g1.add_edge('C','F')
g1.add_edge('F','K')

print(g1.graph)
# print("after deelte")
# g1.delNode('C')
#
print(g1.graph)
print("DFS Traversal")
g1.DFS('A')
print()
print("BFS TRAVERSAL")

g1.BFS('A')
