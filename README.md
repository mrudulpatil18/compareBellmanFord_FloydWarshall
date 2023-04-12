
# Comparison of Bellman Ford and Floyd Warshall Algorithms for All Pair Shortest Paths

#### The Purpose of this project is for an assignment in "DESIGN AND ANALYSIS OF ALGORITHMS" course


This code implements and compares the Bellman Ford and Floyd Warshall algorithms for finding all pair shortest paths in a graph. It measures the runtime of these algorithms on both sparse and dense graphs with varying number of vertices (V).

## Algorithms Implemented

### Bellman Ford Algorithm: 
It is a single-source shortest path algorithm that can handle negative weight edges but does not work with negative weight cycles. The implementation takes a graph as an input, represented as a list of tuples (u, v, w) denoting an edge from vertex u to vertex v with weight w. The algorithm returns a 2D list dist where dist[i][j] represents the shortest path distance from vertex i to vertex j.

### Floyd Warshall Algorithm: 
It is an all pair shortest path algorithm that works with both positive and negative weight edges but does not work with negative weight cycles. The implementation takes a graph as an input, represented as a list of tuples (u, v, w) denoting an edge from vertex u to vertex v with weight w. The algorithm returns a 2D list dist where dist[i][j] represents the shortest path distance from vertex i to vertex j.

## Graph Generation

The code provides two functions for generating graphs:

### generate_sparse_graph(V): 
This function generates a sparse graph with V vertices, where the density of edges can be adjusted by changing the value of the variable E (currently set to V * (V - 1) // 10).
### generate_dense_graph(V): 
This function generates a dense graph with V vertices, which is a complete graph with all possible edges between vertices.

## Runtime Measurement

The code measures the runtime of both algorithms on sparse and dense graphs with varying number of vertices (100, 200, and 400). It uses the time module to measure the runtime of each algorithm and stores the measured times in separate lists (bf_times_sparse, fw_times_sparse, bf_times_dense, and fw_times_dense) for further analysis.

## Results Visualization

The measured runtimes are plotted on a graph using the matplotlib library. The x-axis represents the number of vertices (V), and the y-axis represents the runtime in seconds. The graph shows four lines representing the runtime of Bellman Ford and Floyd Warshall algorithms on both sparse and dense graphs. The legend indicates the type of graph (sparse or dense) and the algorithm used (Bellman Ford or Floyd Warshall). The graph is displayed using the plt.show() function.

#### Note: The graph and results of the runtime analysis can vary depending on the system and environment in which the code is executed.