import time
import random
import matplotlib.pyplot as plt


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
    graph = []

    # Create a cyclic graph with directed edges
    for u in range(V):
        v = (u + 1) % V  # Connect each vertex to the next vertex in a circular manner
        w = random.randint(1, 100)  # Assign random weight to the edge
        graph.append((u, v, w))

    # Add additional edges to increase sparsity
    num_additional_edges = int(0.1 * V)  # 10% of V as additional edges
    for _ in range(num_additional_edges):
        u = random.randint(0, V - 1)  # Randomly choose a source vertex
        v = random.randint(0, V - 1)  # Randomly choose a target vertex
        if u != v and (u, v) not in graph:  # Avoid self-loops and duplicate edges
            w = random.randint(1, 100)  # Assign random weight to the edge
            graph.append((u, v, w))

    return graph


def generate_dense_graph(V):
    #  E = V * (V - 1)   complete graph
    graph = []
    for u in range(V):
        for v in range(V):
            if u != v:  # Avoid self-loops
                w = random.randint(1, 100)  # Assign random weight to the edge
                graph.append((u, v, w))
    return graph


V_range = [100, 200, 500, 1000, 1500, 2000]  # Modify V_range to include larger values
num_iterations = 2  # Increase the number of iterations for each V value

bf_times_sparse = []
fw_times_sparse = []
bf_times_dense = []
fw_times_dense = []

for V in V_range:
    bf_avg_time_sparse = 0
    fw_avg_time_sparse = 0
    bf_avg_time_dense = 0
    fw_avg_time_dense = 0

    for i in range(num_iterations):
        print(V);
        # Generate sparse graph and measure runtime for Bellman-Ford
        graph_sparse = generate_sparse_graph(V)
        start_time = time.time()
        bellman_ford(graph_sparse, V)
        bf_avg_time_sparse += (time.time() - start_time)
        print("Sparse Bellman Ford DONE ......")

        # Generate sparse graph and measure runtime for Floyd-Warshall
        start_time = time.time()
        floyd_warshall(graph_sparse, V)
        fw_avg_time_sparse += (time.time() - start_time)
        print("Sparse Floyd Warshall DONE ......")

        # Generate dense graph and measure runtime for Bellman-Ford
        graph_dense = generate_dense_graph(V)
        start_time = time.time()
        bellman_ford(graph_dense, V)
        bf_avg_time_dense += (time.time() - start_time)
        print("Dense Bellman Ford DONE ......")

        # Generate dense graph and measure runtime for Floyd-Warshall
        start_time = time.time()
        floyd_warshall(graph_dense, V)
        fw_avg_time_dense += (time.time() - start_time)
        print("Dense Floyd Warshall DONE ......")

    # Calculate average runtimes for each algorithm and graph type
    bf_avg_time_sparse /= num_iterations
    fw_avg_time_sparse /= num_iterations
    bf_avg_time_dense /= num_iterations
    fw_avg_time_dense /= num_iterations

    bf_times_sparse.append(bf_avg_time_sparse)
    fw_times_sparse.append(fw_avg_time_sparse)
    bf_times_dense.append(bf_avg_time_dense)
    fw_times_dense.append(fw_avg_time_dense)

# Plot the results for Bellman-Ford
plt.subplot(2, 2, 1)  # Create subplot for sparse graph and Bellman-Ford
plt.plot(V_range, bf_times_sparse, label='Sparse Bellman-Ford')
plt.plot(V_range, bf_times_dense, label='Dense Bellman-Ford')
plt.xlabel('Number of vertices')
plt.ylabel('Time (s)')
plt.legend()
plt.title('Bellman-Ford')

# Plot the results for Floyd-Warshall
plt.subplot(2, 2, 2)  # Create subplot for sparse graph and Floyd-Warshall
plt.plot(V_range, fw_times_sparse, label='Sparse Floyd-Warshall')
plt.plot(V_range, fw_times_dense, label='Dense Floyd-Warshall')
plt.xlabel('Number of vertices')
plt.ylabel('Time (s)')
plt.legend()
plt.title('Floyd-Warshall')

plt.show()
