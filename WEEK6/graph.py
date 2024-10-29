class Graph:
    def __init__(self):
        self.node_count=0
        self.nodes=[]
        self.graph=[]
    def addNode(self,v):
        if v in self.nodes:
            print(f"{v} is already present")
        else:
            self.node_count+=1
            self.nodes.append(v)
            for i in self.graph:
                i.append(0)
            temp=[]
            for i in range(self.node_count):
                temp.append(0)
            self.graph.append(temp)
    def delNode(self,v1):
        print("After deltion")
        if v1 not in self.nodes:
            print(v1," Not in the graph")
        else:
            index=self.nodes.index(v1)
            self.nodes.remove(v1)
            self.node_count-=1
            self.graph.pop(index)
            for i in self.graph:
                i.pop(index)
    def delEdge(self,v1,v2):
        if v1 not in self.nodes or v2 not in self.nodes:
            print("Node is not present in the graph")
        else:
            index1=self.nodes.index(v1)
            index2=self.nodes.index(v2)
            self.graph[index1][index2]=0
            self.graph[index2][index1]=0
    def add_edge(self,v1,v2,cost):
        if v1 not in self.nodes:
            print(v1,"Not present in the graph")
        elif v2 not in self.nodes:
             print(v2,"Not present in the graph")
        else:
            index1=self.nodes.index(v1)
            index2=self.nodes.index(v2)
            self.graph[index1][index2]= cost
            self.graph[index2][index1]= cost



    def printGraph(self):
        print("Vertices are")
        print(self.nodes,end=" ")
        print()
        print("Adjacency Matrix is")
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j],end=" ")
            print()
        print("Number of nodes= ",self.node_count)

g1=Graph()
g1.addNode('A')
g1.addNode('B')
# g1.addNode('D')
g1.addNode('C')
g1.printGraph()
g1.add_edge('A','B',10)
g1.add_edge('A','C',5)
# g1.add_edge('A','D',6)
print("after delete")
g1.printGraph()
# g1.delNode('A')

g1.delEdge("A","B")

g1.printGraph()
print(g1.graph)
