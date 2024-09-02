import math
import os
import random
import re
import sys
import heapq

def find_shortest_route_nodes(n, edges, s):
    # Write your code here
    destinationWeight = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]
    heapDes = []

    destinationWeight[s] = 0

    heapq.heappush(heapDes, (destinationWeight[s], s))
    while len(heapDes) > 0:
        currentWeight, currentDes = heapq.heappop(heapDes)
        if not visited[currentDes]:
            visited[currentDes] = True
            # print("VISIT", currentDes, currentWeight)
            for node in edges[currentDes]:
                if not visited[node]:
                    destinationWeight[node] = min(
                        destinationWeight[node],
                        currentWeight + edges[currentDes][node]
                    )
                    # print(node, destinationWeight[node])
                    heapq.heappush(heapDes, (destinationWeight[node], node))

    # del(destinationWeight[s])

    destinationWeight = list(map(lambda x : -1 if x == math.inf else x, destinationWeight))

    return destinationWeight

class GFG:
    def __init__(self,graph):

        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] >= 0 and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1

        return (result, matchR)

if __name__ == "__main__":
    # fptr = open("input.txt", "r")

    n, m, k = list(map(int, input().rstrip().split()))

    edges = [{} for _ in range(n)]

    for _ in range(m):
        nodeX, nodeY, cost = list(map(int, input().rstrip().split()))
        edges[nodeX - 1][nodeY - 1] = cost
        edges[nodeY - 1][nodeX - 1] = cost

    customers = list(map(int, input().rstrip().split()))
    employees = list(map(int, input().rstrip().split()))

    # fptr.close()

    shortest_route_nodes = []
    for node in range(n):
        shortest_route_nodes.append(find_shortest_route_nodes(n, edges, node))

    # print(shortest_route_nodes)

    shortest_graph = []
    for customer in customers:
        temp_graph = []
        for employee in employees:
            temp_graph.append(shortest_route_nodes[customer - 1][employee - 1])
        shortest_graph.append(temp_graph)

    # print(shortest_graph)

    if k == 1:
        print(shortest_graph[0][0])
        print(1)
    else:
        maximum_graph_distances = []
        for i in range(k):
            for j in range(k):
                maximum_graph_distances.append(shortest_graph[i][j])

        maximum_graph_distances.sort()

        final_result = 0
        final_match_r = []

        low = 0
        high = len(maximum_graph_distances) - 1
        while low < high:
            mid = low + math.floor((high - low) / 2)

            temp_graph = [[0 for _ in range(k)] for _ in range(k)]
            for i in range(k):
                for j in range(k):
                    temp_graph[i][j] = maximum_graph_distances[mid] - shortest_graph[i][j]

            # print(maximum_graph_distances[mid])
            # print(temp_graph)

            g = GFG(temp_graph)

            result, matchR = g.maxBPM()

            # print (result, matchR)

            if result == k:
                final_result = maximum_graph_distances[mid]
                final_match_r = matchR
                high = mid
            else:
                low = mid + 1

        print(final_result)

        for i in range(k):
            final_match_r[i] = str(final_match_r[i] + 1)

        print(" ".join(final_match_r))