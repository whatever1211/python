# Dijkstra
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

# -------------------------------------------------------------------------------------------------------------------
# DFS
# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	
	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	
	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)


# Driver's code
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	
	# Function call
	g.DFS(2)

# This code is contributed by Neelam Yadav

# -------------------------------------------------------------------------------------------------------------------
# BFS
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)

# This code is contributed by Neelam Yadav

# -------------------------------------------------------------------------------------------------------------------
# Cycle detect undirected graph
# Python Program to detect cycle in an undirected graph
from collections import defaultdict

# This class represents a undirected
# graph using adjacency list representation


class Graph:

	def __init__(self, vertices):

		# No. of vertices
		self.V = vertices # No. of vertices

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, v, w):

		# Add w to v_s list
		self.graph[v].append(w)

		# Add v to w_s list
		self.graph[w].append(v)

	# A recursive function that uses
	# visited[] and parent to detect
	# cycle in subgraph reachable from vertex v.
	def isCyclicUtil(self, v, visited, parent):

		# Mark the current node as visited
		visited[v] = True

		# Recur for all the vertices
		# adjacent to this vertex
		for i in self.graph[v]:

			# If the node is not
			# visited then recurse on it
			if visited[i] == False:
				if(self.isCyclicUtil(i, visited, v)):
					return True
			# If an adjacent vertex is
			# visited and not parent
			# of current vertex,
			# then there is a cycle
			elif parent != i:
				return True

		return False

	# Returns true if the graph
	# contains a cycle, else false.

	def isCyclic(self):

		# Mark all the vertices
		# as not visited
		visited = [False]*(self.V)

		# Call the recursive helper
		# function to detect cycle in different
		# DFS trees
		for i in range(self.V):

			# Don't recur for u if it
			# is already visited
			if visited[i] == False:
				if(self.isCyclicUtil
				(i, visited, -1)) == True:
					return True

		return False


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
	print("Graph contains cycle")
else:
	print("Graph doesn't contain cycle ")
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)


if g1.isCyclic():
	print("Graph contains cycle")
else:
	print("Graph doesn't contain cycle ")

# This code is contributed by Neelam Yadav

# -------------------------------------------------------------------------------------------------------------------
# Kruskal Minimum Spanning Tree
# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph


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


# Driver code
if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# Function call
	g.KruskalMST()

# This code is contributed by Neelam Yadav
# Improved by James Graça-Jones

# -------------------------------------------------------------------------------------------------------------------
# Eulerian check
# Python program to check if a given graph is Eulerian or not
#Complexity : O(V+E)

from collections import defaultdict

# This class represents a undirected graph using adjacency list representation


class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	# A function used by isConnected
	def DFSUtil(self, v, visited):
		# Mark the current node as visited
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	'''Method to check if all non-zero degree vertices are
	connected. It mainly does DFS traversal starting from
	node with non-zero degree'''

	def isConnected(self):

		# Mark all the vertices as not visited
		visited = [False]*(self.V)

		# Find a vertex with non-zero degree
		for i in range(self.V):
			if len(self.graph[i]) != 0:
				break

		# If there are no edges in the graph, return true
		if i == self.V-1:
			return True

		# Start DFS traversal from a vertex with non-zero degree
		self.DFSUtil(i, visited)

		# Check if all non-zero degree vertices are visited
		for i in range(self.V):
			if visited[i] == False and len(self.graph[i]) > 0:
				return False

		return True

	'''The function returns one of the following values
	0 --> If graph is not Eulerian
	1 --> If graph has an Euler path (Semi-Eulerian)
	2 --> If graph has an Euler Circuit (Eulerian) '''

	def isEulerian(self):
		# Check if all non-zero degree vertices are connected
		if self.isConnected() == False:
			return 0
		else:
			# Count vertices with odd degree
			odd = 0
			for i in range(self.V):
				if len(self.graph[i]) % 2 != 0:
					odd += 1

			'''If odd count is 2, then semi-eulerian.
			If odd count is 0, then eulerian
			If count is more than 2, then graph is not Eulerian
			Note that odd count can never be 1 for undirected graph'''
			if odd == 0:
				return 2
			elif odd == 2:
				return 1
			elif odd > 2:
				return 0

	# Function to run test cases

	def test(self):
		res = self.isEulerian()
		if res == 0:
			print("graph is not Eulerian")
		elif res == 1:
			print("graph has a Euler path")
		else:
			print("graph has a Euler cycle")


# Let us create and test graphs shown in above figures
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.test()

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
g2.test()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
g3.test()

# Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
g4.test()

# Let us create a graph with all vertices
# with zero degree
g5 = Graph(3)
g5.test()

# This code is contributed by Neelam Yadav

# -------------------------------------------------------------------------------------------------------------------
# Hamiltonian Cycle
# Python program for solution of
# hamiltonian cycle problem

class Graph():
	def __init__(self, vertices):
		self.graph = [[0 for column in range(vertices)]
							for row in range(vertices)]
		self.V = vertices

	''' Check if this vertex is an adjacent vertex
		of the previously added vertex and is not
		included in the path earlier '''
	def isSafe(self, v, pos, path):
		# Check if current vertex and last vertex
		# in path are adjacent
		if self.graph[ path[pos-1] ][v] == 0:
			return False

		# Check if current vertex not already in path
		for vertex in path:
			if vertex == v:
				return False

		return True

	# A recursive utility function to solve
	# hamiltonian cycle problem
	def hamCycleUtil(self, path, pos):

		# base case: if all vertices are
		# included in the path
		if pos == self.V:
			# Last vertex must be adjacent to the
			# first vertex in path to make a cycle
			if self.graph[ path[pos-1] ][ path[0] ] == 1:
				return True
			else:
				return False

		# Try different vertices as a next candidate
		# in Hamiltonian Cycle. We don't try for 0 as
		# we included 0 as starting point in hamCycle()
		for v in range(1,self.V):

			if self.isSafe(v, pos, path) == True:

				path[pos] = v

				if self.hamCycleUtil(path, pos+1) == True:
					return True

				# Remove current vertex if it doesn't
				# lead to a solution
				path[pos] = -1

		return False

	def hamCycle(self):
		path = [-1] * self.V

		''' Let us put vertex 0 as the first vertex
			in the path. If there is a Hamiltonian Cycle,
			then the path can be started from any point
			of the cycle as the graph is undirected '''
		path[0] = 0

		if self.hamCycleUtil(path,1) == False:
			print ("Solution does not exist\n")
			return False

		self.printSolution(path)
		return True

	def printSolution(self, path):
		print ("Solution Exists: Following",
				"is one Hamiltonian Cycle")
		for vertex in path:
			print (vertex, end = " ")
		print (path[0], "\n")

# Driver Code

''' Let us create the following graph
	(0)--(1)--(2)
	| / \ |
	| / \ |
	| /	 \ |
	(3)-------(4) '''
g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
			[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
			[0, 1, 1, 1, 0], ]

# Print the solution
g1.hamCycle();

''' Let us create the following graph
	(0)--(1)--(2)
	| / \ |
	| / \ |
	| /	 \ |
	(3)	 (4) '''
g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
		[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
		[0, 1, 1, 0, 0], ]

# Print the solution
g2.hamCycle();

# This code is contributed by Divyanshu Mehta

# -------------------------------------------------------------------------------------------------------------------
# Hamiltonian Path
# Python3 program for the above approach

# Function to check whether there
# exists a Hamiltonian Path or not
def Hamiltonian_path(adj, N):
	
	dp = [[False for i in range(1 << N)]
				for j in range(N)]

	# Set all dp[i][(1 << i)] to
	# true
	for i in range(N):
		dp[i][1 << i] = True

	# Iterate over each subset
	# of nodes
	for i in range(1 << N):
		for j in range(N):

			# If the jth nodes is included
			# in the current subset
			if ((i & (1 << j)) != 0):

				# Find K, neighbour of j
				# also present in the
				# current subset
				for k in range(N):
					if ((i & (1 << k)) != 0 and
							adj[k][j] == 1 and
									j != k and
						dp[k][i ^ (1 << j)]):
						
						# Update dp[j][i]
						# to true
						dp[j][i] = True
						break
	
	# Traverse the vertices
	for i in range(N):

		# Hamiltonian Path exists
		if (dp[i][(1 << N) - 1]):
			return True

	# Otherwise, return false
	return False

# Driver Code
adj = [ [ 0, 1, 1, 1, 0 ] ,
		[ 1, 0, 1, 0, 1 ],
		[ 1, 1, 0, 1, 1 ],
		[ 1, 0, 1, 0, 0 ] ]

N = len(adj)

if (Hamiltonian_path(adj, N)):
	print("YES")
else:
	print("NO")

# This code is contributed by maheshwaripiyush9
