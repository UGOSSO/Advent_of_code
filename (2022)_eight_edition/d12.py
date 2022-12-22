Input = open("./data/2022/data12.txt", "r")
values = Input.read()
Input.close()

#transform the input in a usable data structure
list_of_values = values.split('\n')
len_line = len(list_of_values[0])
list_of_values = ["."*len_line] + list_of_values + ["."*len_line]
list_of_values = ["." + i + "." for i in list_of_values]
len_line = len(list_of_values[0])

#very rudimentary graph implementation
class Graph() :
    def __init__(self) -> None:
        self.edges = []

    def add_edge(self, v1, v2, weight) :
        if v1 == v2 : raise Exception('same vertex')

        self.edges.append((v1, v2, weight))

    def print_graph(self) :
        for i in self.edges :
            print(i)

#create the graph in order to use Dijktra's algorithm
graph = Graph()

conte, entry, exit = 0, 0, 0
temp1 = []
for i in list_of_values :
    for j in i :
        if  ord(j) == 83 :
            entry = conte 
            j = 'a'
        if ord(j) == 69 : 
            exit = conte
            j = 'z'
        
        if j == '.' : temp1.append([-1, -1])
        else : 
            temp1.append([ord(j), conte])
            conte+=1

list_of_values = temp1

for ind in range(len_line, len(list_of_values)-len_line ) :
    if -1 in list_of_values[ind] : continue 
    else :
        if (-1 not in list_of_values[ind+1]) and list_of_values[ind][0] >= list_of_values[ind+1][0]-1 : 
            graph.add_edge(list_of_values[ind][1], list_of_values[ind+1][1], 1)
        if (-1 not in list_of_values[ind-1]) and list_of_values[ind][0] >= list_of_values[ind-1][0]-1 : 
            graph.add_edge(list_of_values[ind][1], list_of_values[ind-1][1], 1)
        if (-1 not in list_of_values[ind+len_line]) and list_of_values[ind][0] >= list_of_values[ind+len_line][0]-1 : 
            graph.add_edge(list_of_values[ind][1], list_of_values[ind+len_line][1], 1)
        if (-1 not in list_of_values[ind-len_line]) and list_of_values[ind][0] >= list_of_values[ind-len_line][0]-1 : 
            graph.add_edge(list_of_values[ind][1], list_of_values[ind-len_line][1], 1)

#dijktra without returning the path for return path add path in the retrun of line 74
from collections import defaultdict
from heapq import *

def dijkstra(edges, start, end) :
    g = defaultdict(list)
   
    for start_e, end_e, weight in edges:
        g[start_e].append((weight, end_e))

    q, seen = [(0, start, ())], set()
   
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == end : return cost
            for weight, v2 in g.get(v1, ()):
                if v2 not in seen :
                    heappush(q, (cost + weight, v2, path))
   
    return float("inf")

#Part I
resI = dijkstra(graph.edges, entry, exit)

#Part II
entry = [i[1] for i in list_of_values if i[0] == 97]
resII = min([dijkstra(graph.edges, i, exit) for i in entry])

# print(resI) #-> Part I
# print(resII) #-> Part II