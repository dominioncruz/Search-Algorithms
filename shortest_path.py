from collections import deque
import time
# Graph definition
d = {
    "lagos": ["ogun"], 
    "ogun": ["lagos", "osun"], 
    "oyo": ["kwara", "ekiti"], 
    "osun": ["ondo", "ogun"], 
    "ekiti": ["oyo", "imo"],
    "kwara": ["oyo"],
    "ondo": ["osun"],
    "imo": ["ekiti"]
}

def bfs_shortest_path(start: str, goal: str) -> str:

    # Initialize the queue with the start node and the initial path
    queue = deque([(start, [start])])

    # Set to keep track of visited nodes
    visited = set()

    while queue:
        node, path = queue.popleft()  # Use popleft for correct BFS order

        # If the goal node is found, return the path
        if node == goal:
            return return_valid_path(path)

        # Mark the node as visited
        visited.add(node)

        # Iterate over the neighbors of the current node
        for neighbor in d[node]:
            if neighbor not in visited:
                # Append the neighbor and the updated path to the queue
                queue.append((neighbor, path + [neighbor]))

    return "No valid route from {} to {}".format(start.capitalize(), goal.capitalize())  # If no path is found

def return_valid_path(path: list[str]) -> str:
    
    arr = ['|', '/', '-', '\\']
    random_techy_words = ["traversing all routes", "calculating all distance", "best route found", "rerouting to optimal route"]
    
    for i in random_techy_words:
        for j in arr:
            print(f"{i.capitalize().ljust(30)} {j}", end="\r")
            time.sleep(0.3)
    
    path = [place.capitalize() for place in path]
    return "The shortest route to take is: {}".format(" to ".join(path))
        
def get_user_inputs(route_type: str, d: dict) -> str:
    
    while True:
        route = (input(f"Please enter your {route_type} route: ")).strip()
        if route.lower() in d.keys():
            return route
        print("Invalid route, please try again\n")



print("Shortest path finder\n")

start_node = get_user_inputs("start", d)
    
stop_node = get_user_inputs("stop", d)

print(bfs_shortest_path(start_node, stop_node))