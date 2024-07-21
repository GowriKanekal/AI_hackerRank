# DFS 

# Read inputs
pacman_x, pacman_y = list(map(int, input().split())) #pacman co-ordinates 
food_x, food_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))
grid = []
explored = []  # List to store explored nodes
stack = []
answer_routes = None

# input maze
for i in range(0, n): 
    grid.append(list(map(str, input())))

# Possible directions for movement: up, left, right, down
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

# Initialize the queue with Pac-Man's starting position and an empty route
stack.append([pacman_x, pacman_y, []])

# BFS loop
while len(stack) > 0:
    x, y, r = stack.pop()  # Pop the topmost element
    routes = r 
    routes.append([x, y])  # Add the current node to the route

    explored.append([x, y])  # Mark the current node as expanded

    # Check if the current node is the food location
    if x == food_x and y == food_y:
        if answer_routes == None:
            answer_routes = routes
            break

    # Explore neighbors in all four directions
    for d in directions:
        next_x, next_y = x + d[0], y + d[1]
        # to check if neighbours are present within the grid, if not, continue
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue

        # If the neighbor is in the grid, mark it as visited and enqueue it
        if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
            grid[next_x][next_y] = 'v'
            stack.append([next_x, next_y, routes])

# Printing the results
print(str(len(explored)))  # Print the number of explored nodes
for i in explored:
    print(str(i[0]) + " " + str(i[1]))

print(str(len(answer_routes) - 1))  # Print the length of the route to the food
for i in answer_routes:
    print(str(i[0]) + " " + str(i[1]))
