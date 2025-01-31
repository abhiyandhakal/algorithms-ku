import matplotlib.pyplot as plt
import random

from lab2.utils import get_execution_time_min_span


def prims_algorithm(graph):
    # Create a list to store the minimum spanning tree
    mst = []
    # Create a list to store the vertices that have been visited
    visited = []
    # Create a list to store the vertices that have not been visited
    unvisited = list(graph.keys())
    # Choose a starting vertex
    start = unvisited[0]
    # Add the starting vertex to the visited list
    visited.append(start)
    # Remove the starting vertex from the unvisited list
    unvisited.remove(start)
    # While there are still vertices that have not been visited
    while unvisited:
        # Create a list to store the edges that connect visited and unvisited vertices
        edges = []
        # For each vertex in the visited list
        for vertex in visited:
            # For each edge that connects the vertex to another vertex
            for edge in graph[vertex]:
                # If the other vertex is in the unvisited list
                if edge[0] in unvisited:
                    # Add the edge to the list of edges
                    edges.append(edge)
        # Sort the list of edges by weight
        edges.sort(key=lambda x: x[1])
        # Choose the edge with the smallest weight
        edge = edges[0]
        # Add the edge to the minimum spanning tree
        mst.append(edge)
        # Add the other vertex to the visited list
        visited.append(edge[0])
        # Remove the other vertex from the unvisited list
        unvisited.remove(edge[0])
    # Return the minimum spanning tree
    return mst


def krushkals_algorithm(graph):
    # Create a list to store the minimum spanning tree
    mst = []
    # Create a list to store the edges
    edges = []
    # For each vertex in the graph
    for vertex in graph:
        # For each edge that connects the vertex to another vertex
        for edge in graph[vertex]:
            # Add the edge to the list of edges
            edges.append((vertex, edge[0], edge[1]))
    # Sort the list of edges by weight
    edges.sort(key=lambda x: x[2])
    # Create a dictionary to store the sets of vertices
    sets = {}
    # For each vertex in the graph
    for vertex in graph:
        # Create a set with the vertex
        sets[vertex] = {vertex}
    # While there are still edges
    while edges:
        # Choose the edge with the smallest weight
        edge = edges.pop(0)
        # Find the set that contains the first vertex of the edge
        set1 = None
        for key in sets:
            if edge[0] in sets[key]:
                set1 = key
                break
        # Find the set that contains the second vertex of the edge
        set2 = None
        for key in sets:
            if edge[1] in sets[key]:
                set2 = key
                break
        # If the two vertices are in different sets
        if set1 != set2:
            # Add the edge to the minimum spanning tree
            mst.append((edge[0], edge[1], edge[2]))
            # Merge the two sets
            sets[set1] = sets[set1].union(sets[set2])
            # Remove the second set
            del sets[set2]
    # Return the minimum spanning tree
    return mst


def generate_spanning_tree(n):
    """
    Generates a random spanning tree with n nodes in dictionary format.

    :param n: Number of nodes in the tree
    :return: A dictionary representing the spanning tree with weighted edges
    """
    if n < 1:
        raise ValueError("Number of nodes must be at least 1")

    # Generate node labels as uppercase letters
    nodes = [chr(65 + i) for i in range(n)]
    random.shuffle(nodes)
    tree = {node: [] for node in nodes}

    connected = {nodes[0]}
    unconnected = set(nodes[1:])

    while unconnected:
        u = random.choice(list(connected))
        v = random.choice(list(unconnected))
        weight = random.randint(1, 10)

        tree[u].append((v, weight))
        tree[v].append((u, weight))

        connected.add(v)
        unconnected.remove(v)

    return tree


test_lens = [5, 10, 17, 25, 50, 100, 200, 500]
y_values_prims = []
y_values_krushkals = []

for n in test_lens:
    graph = generate_spanning_tree(n)
    y_values_krushkals.append(
        get_execution_time_min_span(krushkals_algorithm, graph))
    y_values_prims.append(get_execution_time_min_span(prims_algorithm, graph))


# Plot
plt.xlabel('Number of nodes')
plt.ylabel('Execution time')
plt.title('Minimum Spanning Tree Problem')
plt.plot(test_lens, y_values_prims, label='Prims')
plt.plot(test_lens, y_values_krushkals, label='Krushkals')
plt.grid(True)
plt.legend()
plt.show()
