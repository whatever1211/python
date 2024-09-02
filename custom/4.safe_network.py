import math
import os
import random
import re
import sys

node_count = 0

def dfs(cur_node, edges, stack_arr, is_in_stack, result_scc, visited):
    global node_count
    cur_node_count = node_count
    result_scc[cur_node] = node_count
    visited[cur_node] = True
    stack_arr.append(cur_node)
    is_in_stack[cur_node] = True
    node_count += 1

    # print("--------", end="\n")
    # print(cur_node_count, end="\n")
    # print(cur_node, end="\n")
    # print(edges, end="\n")

    for node in edges[cur_node]:
        if edges[cur_node][node] > 0:
            edges[cur_node][node] -= 1
            edges[node][cur_node] -= 1
            if visited[node]:
                if is_in_stack[node]:
                    result_scc[cur_node] = min(result_scc[cur_node], result_scc[node])
            else:
                dfs(node, edges, stack_arr, is_in_stack, result_scc, visited)
                result_scc[cur_node] = min(result_scc[cur_node], result_scc[node])

    if result_scc[cur_node] == cur_node_count:
        while True:
            stack_node = stack_arr.pop()
            result_scc[stack_node] = cur_node_count
            is_in_stack[stack_node] = False
            if stack_node == cur_node:
                break

def get_scc_arr(n, edges):
    stack_arr = []
    result_scc = {}
    visited = [False] * n
    is_in_stack = [False] * n

    first_node = 0
    dfs(first_node, edges, stack_arr, is_in_stack, result_scc, visited)

    return result_scc

def get_bridges(edges, scc_arr):
    scc_count = {}

    for x, y in edges:
        if scc_arr[x] != scc_arr[y]:
            if scc_arr[x] in scc_count:
                scc_count[scc_arr[x]] += 1
            else:
                scc_count[scc_arr[x]] = 1
            if scc_arr[y] in scc_count:
                scc_count[scc_arr[y]] += 1
            else:
                scc_count[scc_arr[y]] = 1

    scc_one_bridge_count = 0
    for node in scc_count:
        if (scc_count[node]) == 1:
            scc_one_bridge_count += 1

    # print(edges)
    # print(scc_count)

    return scc_one_bridge_count // 2 + scc_one_bridge_count % 2

if __name__ == "__main__":
    # fptr = open("input.txt", "r")

    n, m = list(map(int, input().rstrip().split()))

    edges = [{} for _ in range(n)]

    raw_edges = []

    for _ in range(m):
        nodeX, nodeY = list(map(int, input().rstrip().split()))
        if (nodeX == nodeY):
            continue
        raw_edges.append((nodeX - 1, nodeY - 1))
        if (nodeY - 1) not in edges[nodeX - 1]: edges[nodeX - 1][nodeY - 1] = 1
        else: edges[nodeX - 1][nodeY - 1] = 2
        if (nodeX - 1) not in edges[nodeY - 1]: edges[nodeY - 1][nodeX - 1] = 1
        else: edges[nodeY - 1][nodeX - 1] = 2

    # print(edges)

    # fptr.close()

    scc_arr = get_scc_arr(n, edges)

    # print(scc_arr)

    result = get_bridges(raw_edges, scc_arr)

    print(result)