import time
import random
import matplotlib.pyplot as plt
import numpy as np


def bellman_ford(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    for u, v, w in graph:
        dist[u][v] = w
    for u in range(V):
        dist[u][u] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def floyd_warshall(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    for u in range(V):
        dist[u][u] = 0
    for u, v, w in graph:
        dist[u][v] = w
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def generate_sparse_graph(V):
    E = V * (V - 1) // 10  # Adjust density as desired
    graph = []
    while len(graph) < E:
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)
        w = random.randint(1, 100)
        if u != v and (u, v, w) not in graph:
            graph.append((u, v, w))
    return graph


def generate_dense_graph(V):
    E = V * (V - 1) // 2  # Complete graph
    graph = []
    while len(graph) < E:
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)
        w = random.randint(1, 100)
        if u != v and (u, v, w) not in graph:
            graph.append((u, v, w))
    return graph


V_range = [100, 200, 400, 600, 800, 1000, 1500, 2000, 2500]
bf_times_sparse = []
fw_times_sparse = []
bf_times_dense = []
fw_times_dense = []

for V in V_range:
    # Generate sparse graph and measure runtime for Bellman-Ford
    graph_sparse = generate_sparse_graph(V)
    start_time = time.time()
    bellman_ford(graph_sparse, V)
    bf_times_sparse.append(time.time() - start_time)

    # Generate sparse graph and measure runtime for Floyd-Warshall
    start_time = time.time()
    floyd_warshall(graph_sparse, V)
    fw_times_sparse.append(time.time() - start_time)

    # Generate dense graph and measure runtime for Bellman-Ford
    graph_dense = generate_dense_graph(V)
    start_time = time.time()
    bellman_ford(graph_dense, V)
    bf_times_dense.append(time.time() - start_time)

    # Generate dense graph and measure runtime for Floyd-Warshall
    start_time = time.time()
    floyd_warshall(graph_dense, V)
    fw_times_dense.append(time.time() - start_time)

plt.plot(V_range, bf_times_sparse, label='Sparse Bellman-Ford')
plt.plot(V_range, fw_times_sparse, label='Sparse Floyd-Warshall')
plt.plot(V_range, bf_times_dense, label='Dense Bellman-Ford')
plt.plot(V_range, fw_times_dense, label='Dense Floyd-Warshall')
plt.xlabel('Number of vertices')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
