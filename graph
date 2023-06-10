###
Input Format
The first line contains t, the number of test cases.
Each test case is as follows:
- The first line contains two space-separated integers n and m, the number of nodes and edges in the graph.
- Each of the next lines contains three space-separated integers x, y, and r, the beginning and ending nodes of an edge, and the length of the edge.
- The last line of each test case has an integer s, denoting the starting position.

If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format
For each of the t test cases, print a single line consisting n - 1 space separated integers denoting the shortest distance to the n - 1 nodes from starting position s in increasing order of their labels, excluding s.
For unreachable nodes, print -1.

Sample Input
1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1

Sample Output
24 3 15
###

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    # Write your code here
    print(edges)
    destinationWeight = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]
    heapDes = []
    
    destinationWeight[s] = 0
    
    heapq.heappush(heapDes, (destinationWeight[s], s))
    while len(heapDes) > 0:
        currentWeight, currentDes = heapq.heappop(heapDes)
        if not visited[currentDes]:
            visited[currentDes] = True
            print("VISIT", currentDes, currentWeight)            
            for node in edges[currentDes]:
                if not visited[node]:
                    destinationWeight[node] = min(
                        destinationWeight[node],
                        currentWeight + edges[currentDes][node]
                    )                
                    print(node, destinationWeight[node])    
                    heapq.heappush(heapDes, (destinationWeight[node], node))           
                    
    del(destinationWeight[s])
    
    destinationWeight = map(lambda x : -1 if x == math.inf else x, destinationWeight)
    
    return destinationWeight    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = [{} for _ in range(n)]            

        for _ in range(m):
            nodeX, nodeY, weight = list(map(int, input().rstrip().split()))
            if (nodeY - 1) not in edges[nodeX - 1]: edges[nodeX - 1][nodeY - 1] = weight
            else: edges[nodeX - 1][nodeY - 1] = min(weight, edges[nodeX - 1][nodeY - 1])
            if (nodeX - 1) not in edges[nodeY - 1]: edges[nodeY - 1][nodeX - 1] = weight
            else: edges[nodeY - 1][nodeX - 1] = min(weight, edges[nodeY - 1][nodeX - 1])
            
            
        s = int(input().strip())          

        result = shortestReach(n, edges, s - 1)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
