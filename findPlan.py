import os
workingFolder = "example-problems" 
#directory = os.fsencode("problems")
directory = os.fsencode(workingFolder)

# solution = ""

#__FUNCTIONS__ 

def goNorth(agent):
    #print("Go North")
    if agent[0] == 0: 
        agent[0] = 11
    else: 
        #Decrease Y by one
        agent[0] = agent[0]-1 
    return agent 

def goSouth(agent): 
    #print("Go South")
    if agent[0] == 11: 
        agent[0] = 0
    else: 
        #Increase Y by one
        agent[0] = agent[0]+1 
    return agent 

def goWest(agent):
    #print("Go west")
    if agent[1] == 0: 
        agent[1] = 17
    else: 
        #Decrease X by one
        agent[1] = agent[1]-1 
    return agent 

def goEast(agent):
    #print("Go East")
    if agent[1] == 17: 
        agent[1] = 0
    else: 
        #Increase X by one
        agent[1] = agent[1]+1 
    return agent 



def is_valid_move_dfs(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'X' and (x, y) not in visited

def get_direction(current, next_pos):
    x_curr, y_curr = current
    x_next, y_next = next_pos
    #print(current, next_pos)
    if x_next == x_curr + 1:
        return 'N'
    elif x_next == x_curr - 1:
        return 'S'
    elif y_next == y_curr + 1:
        return 'W'
    elif y_next == y_curr - 1:
        return 'E'
    elif x_next == 0:
        return 'N'
    elif x_next == 11:
        return 'S'
    elif y_next == 0:
        return 'W'
    elif y_next == 17:
        return 'E'



def dfs(maze, current_position, goal, visited, path):
    x, y = current_position

    if current_position == goal:
        path.append(current_position)
        return True

    visited.add(current_position)
    
    #for neighbor in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    for neighbor in [tuple(goSouth(list(current_position))),tuple(goNorth(list(current_position))), tuple(goWest(list(current_position))), tuple(goEast(list(current_position)))]:
        if is_valid_move_dfs(maze, *neighbor, visited):
           # print("")
           # print("Agent: " ,current_position, "neighbor: ", neighbor )
            if dfs(maze, neighbor, goal, visited, path):
                path.append(current_position)
                return True

    # If all neighbors are visited or walls, backtrack
    #visited.remove(current_position)
    return False



def find_solution_with_S(plan):
    with open('mySolutions/solution_' + X + '_' + YZ, 'w') as f:
        if plan:
            f.write(''.join(plan))
        else:
            f.write('NO PATH FOUND\n') 


def finPlan(maze, start):
    
    # TODO: Change empty position variable with the find_mapElements variable 
    empty_positions = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == ' ']
    print("empty_positions: ", empty_positions)
    visited_set = set()
    path = []
    all_paths_coordinates = []

    for goal in empty_positions:
        if not dfs(maze, start, goal, visited_set, path):
            print("No path found to goal at", goal)
            return

        path_coordinates = [get_direction(path[i], path[i + 1]) for i in range(len(path) - 1)]
        print(path_coordinates)
        if path_coordinates != None:
            path_coordinates_str = ''.join(path_coordinates[::-1])
        
        print("\nPath found to goal at", goal, "as coordinates:", path_coordinates_str)
        print("Path found to goal at", goal, "as coordinates (full):", path[::-1])

        # Update start_position to the reached goal
        start = goal

        # Accumulate path coordinates
        all_paths_coordinates.append(path_coordinates_str)
        # Print all concatenated path coordinates at the end
        print("\nAll paths coordinates:", ''.join(all_paths_coordinates))
        find_solution_with_S(''.join(all_paths_coordinates))
        # Clear visited set and path for the next iteration
        visited_set.clear()
        path.clear()



def find_mapElements(_map):
    indices = []
    agent = [] 
    
    #find the empty squares and the agent locations
    for row_index, row in enumerate (_map):
        for col_index, element in enumerate (row):
            #print(element, end=' ')
            #print()
            if element == ' ':       
                indices.append((row_index, col_index))
            elif element == 'S': 
                agent.append(row_index)
                agent.append(col_index)

    indices.append(tuple(agent))
    #print(indices)
    return (indices, agent)

#__MAIN__

# Open the file for reading
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    l = filename.split("_")
    X = l[1]
    YZ = l[2]

    #if X == 'e' and YZ == '00.txt':
    if X == 'e':
    #if X == 'a' or X == 'b' or X == 'c' or X == 'd':
        with open(workingFolder + '\\' + filename, 'r') as file2:
            # Read the first line
            line = file2.readlines()
            _map = [item.replace('\n', "") for item in line]
            
            # Extract the first line (type of the problem)
            problemType = _map[0]

        if problemType == "FIND PLAN":
            print("Find")

            sample_maze = _map[1:]
            print("sample_maze: ", sample_maze)
            # emptySquares, agent = find_mapElements(cave)
            # solution = findPlan(emptySquares.copy(), agent.copy())
            # find_solution_with_S(solution)
            # print("Solution:", solution)

            # Write the solution to a file
            _ , agent = find_mapElements(sample_maze)
            start_position = tuple(agent)
            # start_position = (5, 3)
            #goal_position = (3, 3)
            # path_dfs = find_path_dfs(sample_maze, start_position, goal_position)
            path_dfs = finPlan(sample_maze, start_position)
            #print("solution: ",solution )
            if path_dfs:
                print("\nPath found:", path_dfs)
            else:
                print("\nNo path found.")