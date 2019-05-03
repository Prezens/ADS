import networkx as nx
import matplotlib.pyplot as plt
import csv
import DFS_graphs
import BFS_graphs


G = nx.Graph()

data_graph = []
vortexs = {}


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        data_graph.append(row)


csv_path = 'data_graph.csv'
with open(csv_path, 'r') as file:
    csv_reader(file)

# G.add_nodes_from(n)

for graph in data_graph:
    if graph[0] not in vortexs.keys():
        vortexs[graph[0]] = [graph[1]]
    else:
        vortexs[graph[0]].append(graph[1])

    if graph[1] not in vortexs.keys():
        vortexs[graph[1]] = [graph[0]]
    else:
        vortexs[graph[1]].append(graph[0])

print(vortexs, '\n')

explored_DFS, protocol_DFS = DFS_graphs.dfs(vortexs, '1')
print(explored_DFS, '\n')
print('\n'.join(protocol_DFS))

explored_BFS, protocol_BFS = BFS_graphs.bfs(vortexs, '1')
print(explored_BFS, '\n')
print('\n'.join(protocol_BFS))

G.add_edges_from(data_graph)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()


if __name__ == '__main__':
    pass
