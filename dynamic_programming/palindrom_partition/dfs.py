


def dfs(Graph, start_node):

    visited = [False for _ in range(len(Graph))]

    visited[start_node] = True
    order = [start_node]

    for neighbour in Graph[start_node]:
        if not visited[neighbour]:
            order.append(neighbour)
            dfs(Graph, neighbour)

    return order