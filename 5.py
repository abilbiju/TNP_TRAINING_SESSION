#5. write a program to identify the cycle in a graph
# eg:n=7
# 1-2
# 2-3
# 3-4
# 4-5
# 4-6
# 3-1
# output: True 
# at 1-2-3-1

n=int(input())
edges={}
visited=[]

def detectLoop(node):
    if visited[node]:
        visited[node]=True
        nextItems=edges[node]
        for i in nextItems:
            if detectLoop(i):
                return True
        return False
    else:
        return True 
    
for i in range(n):
    ListOfNodes=[]
    a,b=list(map(int,input().rstrip().split(' ')))
    ListOfNodes.append(a)
    ListOfNodes.append(b)
    if a in edges.keys():
        edges[a].append(b)
    else:
        edges[a] = [b]
ListOfNodes=list(set(ListOfNodes))
numberOfNodes=len(ListOfNodes)
visited=[False]*numberOfNodes

detectLoop(edges.keys()[0])

#print(edges)