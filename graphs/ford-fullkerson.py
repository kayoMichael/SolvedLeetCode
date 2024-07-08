import unittest
from collections import deque

infinity = float("inf")

"""

Core Algorithm: Find the Residual Graph, and repeatedly find augmenting paths (s-t paths) in the residual graph 
                from source node to sink node. For each path found, push the maximum possible flow along it, 
                limited by the minimum residual capacity of the path. After each flow augmentation, decrease forward 
                edge capacities and increase reverse edge capacities. Repeat until no augmenting path exists in the
                residual graph. The maximum flow is the total flow pushed from sink node (s) to source node (t)
                The st-min cut is the remaining arcs that are reachable from s in the residual graph (not full capacity)
                
"""


def node_label(i, source, sink):
    if i == source:
        return 's'
    elif i == sink:
        return 't'
    else:
        return str(i)


def bfs(G, source, sink, parent):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    print("\nStarting BFS:")
    print(f"Source: {node_label(source, source, sink)}, Sink: {node_label(sink, source, sink)}")

    while queue:
        node = queue.popleft()
        print(f"Exploring node {node_label(node, source, sink)}")

        for i in range(len(G[node])):
            if i not in visited and G[node][i] > 0:
                queue.append(i)
                visited.add(i)
                parent[i] = node
                print(
                    f"  Found path: {node_label(node, source, sink)} -> {node_label(i, source, sink)} (capacity: {G[node][i]})")

    if sink in visited:
        print("Path to sink found!")
    else:
        print("No path to sink found.")
    return sink in visited


def ford_fulkerson(G, source, sink):
    parent = [-1] * (len(G))
    max_flow = 0
    iteration = 1

    while bfs(G, source, sink, parent):
        print(f"\n--- Iteration {iteration} ---")
        path_flow = infinity
        s = sink
        path = []

        while s != source:
            path.append(node_label(s))
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
        path.append(node_label(source, source, sink))
        path.reverse()

        print(f"Augmenting path: {' -> '.join(path)}")
        print(f"Path flow: {path_flow}")

        max_flow += path_flow
        v = sink

        print("Updating residual graph:")
        while v != source:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            print(f"  Edge {node_label(u, source, sink)} -> {node_label(v, source, sink)}: capacity now {G[u][v]}")
            print(f"  Edge {node_label(v, source, sink)} -> {node_label(u, source, sink)}: capacity now {G[v][u]}")
            v = parent[v]

        iteration += 1

    return max_flow


def print_final_flow(original_graph, residual_graph, source, sink):
    print("\nFinal Flow:")
    for i in range(len(original_graph)):
        for j in range(len(original_graph[i])):
            if original_graph[i][j] > 0:
                flow = original_graph[i][j] - residual_graph[i][j]
                if flow > 0:
                    print(f"Edge {node_label(i, source, sink)} -> {node_label(j, source, sink)}: Flow = {flow}")


def find_min_cut(G, source, sink):
    def dfs(node, visited):
        visited.add(node)
        for next_node in range(len(G)):
            if G[node][next_node] > 0 and next_node not in visited:
                dfs(next_node, visited)

    reachable = set()
    dfs(source, reachable)

    min_cut = []
    for u in reachable:
        for v in range(len(G)):
            if v not in reachable and G[u][v] == 0 and G[v][u] > 0:
                min_cut.append((u, v))

    print("\nMinimum s-t cut:")
    print("S =", {node_label(node) for node in reachable})
    print("T =", {node_label(node) for node in range(len(G)) if node not in reachable})
    print("Cut edges:")
    for u, v in min_cut:
        print(f"  {node_label(u)} -> {node_label(v)}")

    return min_cut


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self) -> None:
        # S, 1,2,3,4,5,6,7,8,9,T
        self.graph = [
            [0, 0, 0, 0, 1, 0, 0, 10, 3, 20, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15],
            [0, infinity, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, infinity, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, infinity, 0, 0, 0, 0, 0, 0, 3],
            [0, infinity, 0, 0, 0, infinity, 0, 0, 0, 0, 0],
            [0, infinity, infinity, infinity, 0, infinity, infinity, 0, 0, 0, 0],
            [0, 0, 0, infinity, 0, 0, infinity, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def test_LastWordLength(self):
        self.assertEqual(ford_fulkerson(self.graph, 0, 10), 32)
        self.assertEqual(find_min_cut(self.graph, 0, 10), [(0, 4), (0, 7), (0, 8), (3, 8), (3, 10), (6, 8), (6, 10)])


if __name__ == '__main__':
    unittest.main()
