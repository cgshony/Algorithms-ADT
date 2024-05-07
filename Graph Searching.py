from collections import deque

"""Breadth-first search on a graph starting from a specified node.

   Args - graph (dict): The graph represented as an adjacency list.
        - source (str): The starting node."""

def bfs(graph,source):

    visited = set()     #to keep track of visited nodes
    queue = deque([source])
    distances = {source: 0}         #to store distances from the source and predecessors for each node
    predecessors = {source: None}

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()

        # Explore neighbors of the current vertex
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                distances[neighbour] = distances[vertex] +1 # store distance from the source to the neighbor
                predecessors[neighbour] = vertex

    return distances, predecessors


def shortest_path(predecessors, destination):
    """# Function to find the shortest path from predecessors dictionary"""
    path = []
    vertex = destination
    # Retreive the shortest path from destination to source
    while vertex is not None:
        path.append(vertex)
        vertex = predecessors[vertex]
    return path[::-1]



"""Depth First Search implementation"""

def dfs(graph, start, end):

    stack = [(start, [start])]  # start vertex and the path containing the start vertex
    visited = set()  # Initialize an empty set for visited vertices

    while stack:
        vertex, path = stack.pop()  # Pop the vertex and corresponding path
        if vertex not in visited:
            if vertex == end:
                return path  # Return the path if the end vertex is reached
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))  # Update with the current neighbour

    return False  #if the end vertex can't be reached


if __name__=='__main__':
    graph = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]
    }

    start_vertex = 'A'
    print('Distances from the source node to each node in the graph, predecessors for each visited node visited:\n', bfs(graph, start_vertex))

    distances, predecessors = bfs(graph, start_vertex)
    destination_vertex = 'F'
    shortest_path_to_destination = shortest_path(predecessors, destination_vertex)
    print("Shortest path to", destination_vertex, ":", shortest_path_to_destination)

    print('DFS implementation: ')
    path = dfs(graph,start_vertex,destination_vertex)
    print(f"Path from {start_vertex} to {destination_vertex} :{path} ")