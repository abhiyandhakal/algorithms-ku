import matplotlib.pyplot as plt
import random
from lab2.utils import get_execution_time_min_span


def prims_algorithm(graph):
    mst, visited, unvisited = [], [], list(graph.keys())
    start = unvisited.pop(0)
    visited.append(start)

    while unvisited:
        edges = [(v, e)
                 for v in visited for e in graph[v] if e[0] in unvisited]
        edge = min(edges, key=lambda x: x[1][1])
        mst.append(edge[1])
        visited.append(edge[1][0])
        unvisited.remove(edge[1][0])

    return mst


def krushkals_algorithm(graph):
    mst, edges, sets = [], [], {v: {v} for v in graph}

    for v in graph:
        for e in graph[v]:
            edges.append((v, e[0], e[1]))
    edges.sort(key=lambda x: x[2])

    while edges:
        u, v, w = edges.pop(0)
        set_u, set_v = None, None

        for key in sets:
            if u in sets[key]:
                set_u = key
            if v in sets[key]:
                set_v = key

        if set_u != set_v:
            mst.append((u, v, w))
            sets[set_u].update(sets[set_v])
            del sets[set_v]

    return mst


def generate_spanning_tree(n):
    if n < 1:
        raise ValueError("Number of nodes must be at least 1")

    nodes = [chr(65 + i) for i in range(n)]
    random.shuffle(nodes)
    tree = {node: [] for node in nodes}

    connected, unconnected = {nodes[0]}, set(nodes[1:])

    while unconnected:
        u, v = random.choice(list(connected)), random.choice(list(unconnected))
        weight = random.randint(1, 10)

        tree[u].append((v, weight))
        tree[v].append((u, weight))

        connected.add(v)
        unconnected.remove(v)

    return tree


test_lens = [5, 10, 17, 25, 50, 100, 200, 500]
y_values_prims, y_values_krushkals = [], []

for n in test_lens:
    graph = generate_spanning_tree(n)
    y_values_krushkals.append(
        get_execution_time_min_span(krushkals_algorithm, graph))
    y_values_prims.append(get_execution_time_min_span(prims_algorithm, graph))

plt.xlabel('Number of nodes')
plt.ylabel('Execution time')
plt.title('Minimum Spanning Tree Problem')
plt.plot(test_lens, y_values_prims, label='Prims')
plt.plot(test_lens, y_values_krushkals, label='Krushkals')
plt.grid(True)
plt.legend()
plt.show()
