# -------------------------------------------------------------------------------------------------------------------
# 1. Journey to the Moon
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000 * 1000)

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def dfs(start, astronaut, check, nation, curNation):
    if check[start]:
        return
    check[start] = True
    nation[start] = curNation
    for i in astronaut[start]:
        if not check[i]:
            dfs(i, astronaut, check, nation, curNation)

def journeyToMoon(n, astronaut):
    # Write your code here
    check = [False] * n
    nation = [-1] * n
    curNation = 0
    
    for i in range(n):
        if not check[i]:
            curNation += 1
            dfs(i, astronaut, check, nation, curNation)
    
    print(check)
    print(nation)
    print(curNation)
            
    countNationAstro = [0] * curNation
    for i in range(n):
        countNationAstro[nation[i] - 1] += 1        
            
    sumCurNation = sum(countNationAstro)
    result = 0
    for i in range(curNation - 1):
        result += countNationAstro[i] * (sumCurNation - countNationAstro[i])
        sumCurNation -= countNationAstro[i]        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])
    
    astronaut = [{} for _ in range(n)]

    for _ in range(p):
        nodeX, nodeY = list(map(int, input().rstrip().split()))
        if nodeY not in astronaut[nodeX]: astronaut[nodeX][nodeY] = True
        if nodeX not in astronaut[nodeY]: astronaut[nodeY][nodeX] = True
    
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

# -------------------------------------------------------------------------------------------------------------------
# 2. Roads and Libraries
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000 * 1000)

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def dfs(start, cities, check, city, curCity):
    if check[start]:
        return
    check[start] = True
    city[start] = curCity
    for i in cities[start]:
        if not check[i]:
            dfs(i, cities, check, city, curCity)

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    
    if c_lib <= c_road:
        return c_lib * n
    
    check = [False] * n
    city = [-1] * n    
    curCity = 0
    
    for i in range(n):
        if not check[i]:
            curCity += 1
            dfs(i, cities, check, city, curCity)
            
    countCityNode = [0] * curCity
    for i in range(n):
        countCityNode[city[i] - 1] += 1
        
    print(check)
    print(city)
    print(curCity)    
    print(countCityNode)
    
    result = 0
    for i in range(curCity):
        result += c_road * (countCityNode[i] - 1)
    
    result += c_lib * curCity
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = [{} for _ in range(n)]

        for _ in range(m):
            nodeX, nodeY = list(map(int, input().rstrip().split()))
            if (nodeY - 1) not in cities[nodeX - 1]: cities[nodeX - 1][nodeY - 1] = True            
            if (nodeX - 1) not in cities[nodeY - 1]: cities[nodeY - 1][nodeX - 1] = True            

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

# -------------------------------------------------------------------------------------------------------------------
# 3. Kruskal (MST): Really Special Subtree
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:

            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST
    # using Kruskal's algorithm
    def KruskalMST(self):

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
        
        return minimumCost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    g = Graph(g_nodes)
    
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())
        g.addEdge(g_from[i] - 1, g_to[i] - 1, g_weight[i])

    g.KruskalMST()    

    fptr.write(str(g.KruskalMST()))

    fptr.close()
