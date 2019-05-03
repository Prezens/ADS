def dfs(graph, start):
    protocol = []
    explored, stack = set(), [start]
    explored.add(start)

    while stack:
        v = stack.pop()
        protocol.append(str('Explored vortex ' + v))
        for w in graph[v]:
            protocol.append(str('In ' + v + ' : ' + w))
            if w not in explored:
                explored.add(w)
                stack.append(w)

    return explored, protocol


if __name__ == '__main__':
    G = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    print(dfs(G, 'A'))
