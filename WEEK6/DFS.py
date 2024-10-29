class Graph:
   def __init__(self):
       self.node_count=0
       self.visited=set()
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
           # list1=[v2]
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
           print(v)
           self.visited.add(v)
           for i in self.graph[v]:
               self.DFS(i)


g1=Graph()
g1.add_node('A')
g1.add_node('B')
g1.add_node('C')
g1.add_node('D')
g1.add_node('E')
g1.add_edge('A','B')
g1.add_edge('B','E')
g1.add_edge('A','C')
g1.add_edge('A','D')
g1.add_edge('B','D')
g1.add_edge('C','D')
g1.add_edge('E','D')
print(g1.graph)
print("after deelte")
g1.delNode('C')
#
print(g1.graph)
print("DFS Traversal")
g1.DFS('E')
