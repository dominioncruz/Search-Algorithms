# Importing the deque class from the collections module
from collections import deque


# Defining the breadth-first search (BFS) function
def bfs(node):
    # Defining the adjacency list for the graph
    d = {
        0: [1, 2],
        1: [0, 2, 4],
        2: [0, 1, 3],
        3: [2],
        4: [1]
    }

    # A set to keep track of visited nodes
    visited = set()

    # Initializing a queue using deque
    queue = deque()

    # Adding the starting node to the queue and marking it as visited
    queue.appendleft(node)
    visited.add(node)

    # Looping until the queue is empty
    while queue:
        # Popping a node from the queue
        v = queue.pop()

        # Printing the current node
        print(v)

        # Retrieving the list of adjacent nodes
        inner_list = d[v]

        # Iterating through each adjacent node
        for i in inner_list:
            # If the node has not been visited, add it to the queue and mark as visited
            if i not in visited:
                queue.appendleft(i)
                visited.add(i)


# Calling the BFS function starting from node 0
bfs(0)
