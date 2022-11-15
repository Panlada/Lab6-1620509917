from msilib import Table


class graph:
    def __init__(self):
        self.x = [[" "," "],[" "," "]]
    def create_edge(self,Node_name):
        temp = self.x[0]
        if self.x[0][-1] != " ":
            self.x[0].append(" ")
            Firstime = False
        else:
            Firstime = True
        check = 0
        if self.x[0][0] == " ":
            self.x[0][0] = "-"
        for i in range (len(self.x[0])):
            if i == len(self.x[0])- 1 and not Firstime:
                self.x.append([])
            while len(self.x[i]) < len(self.x[i-1]):
                self.x[i].append("0")
                if self.x[i][0] == "0":
                    self.x[i][0] = " "
        for i in range (len(self.x)):
            if self.x[0][i] == " " and check == 0:
                    self.x[0][i] = Node_name
                    check = 1
        for j in range (len(self.x[0])):
            if self.x[j][0] == " " and check == 1:
                self.x[j][0] = Node_name
                self.x[j][1] = "0"
                check = 0
    def Adjacency_Matrix(self):
        print(len(self.x) * "=")
        for i in range(len(self.x)):
            print(self.x[i])
    def connect(self,NodeA,NodeB):
        if NodeA in self.x[0] and NodeB in self.x[0] :
            NodeAIndex,NodeBIndex = 0,0
            for i in range(len(self.x)):
                if NodeA == self.x[0][i]:
                    NodeAIndex = i
                elif NodeB == self.x[0][i]:
                    NodeBIndex = i
                self.x[NodeAIndex][NodeBIndex] = "1"
                self.x[NodeBIndex][NodeAIndex] = "1"
        else:
            print ("Not")
    def Adjacency_List(self): 
        tempList = [] 
        for i in range(1,len(self.x)): 
            tempList.append(str(self.x[i][0]) + ":") 
            for j in range(1,len(self.x)): 
                if self.x[i][j] == "1": 
                    tempList.append(self.x[0][j])
            print(tempList)
            tempList=[]
    def Edge_List(self): 
        tempList = [ ] 
        memList = [ ] 
        output = [[ ],[ ]] 
        for i in range(1,len(self.x)): 
            tempList.append(str(self.x[i][0]) + ":") 
            memList.append(self.x[i][0]) 
            for j in range(1,len(self.x)): 
                if self.x[i][j] == "1": 
                    tempList.append(self.x[0][j]) 
                    memCheck = len(memList) 
                    memList[memCheck-1] += self.x[0][j] 
                    if j != (len(self.x) - 1): 
                        memList.append(self.x[i][0])
                elif (j == (len(self.x) - 1) and self.x[i][j] == "0"):
                    memList.pop()

#### Create A,B,C,D,E,F
TableA =graph()
TableA.create_edge("A")
TableA.create_edge("B")
TableA.create_edge("C")
TableA.create_edge("D")
TableA.create_edge("E")
TableA.create_edge("F")
### connect AB,AC,CD,CF,EF
TableA.connect("A","B")
TableA.connect("A","C")
TableA.connect("C","D")
TableA.connect("C","F")
TableA.connect("E","F")
TableA.Adjacency_Matrix()
TableA.Adjacency_List()
TableA.Edge_List()

## Disconnect
print("#########################DISCONNECTPART####################################")
TableA1 = graph()
TableA1.create_edge("A")
TableA1.create_edge("B")
TableA1.create_edge("C")
TableA1.create_edge("D")
TableA1.create_edge("E")
TableA1.create_edge("F")
### connect AB,AC,CD,CF,EF
TableA1.connect("A","C")
TableA1.connect("E","F")
TableA1.Adjacency_Matrix()
TableA1.Adjacency_List()
TableA1.Edge_List()

## reconnect

print("#########################RECONNECTPART####################################")
TableA2 = graph()
TableA2.create_edge("A")
TableA2.create_edge("B")
TableA2.create_edge("C")
TableA2.create_edge("D")
TableA2.create_edge("E")
TableA2.create_edge("F")
### connect AB,AC,CD,CF,EF
TableA2.connect("A","E")
TableA2.connect("B","C")
TableA2.connect("D","F")
TableA2.Adjacency_Matrix()
TableA2.Adjacency_List()
TableA2.Edge_List()