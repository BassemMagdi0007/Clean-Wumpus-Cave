import os
workingFolder = "problems" 
#directory = os.fsencode("problems")
directory = os.fsencode(workingFolder)

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

def write_solution_with_S(myDict):
    valid = 1
    for item in myDict:
        if myDict[item] == 'open':   
            valid = 0        
            print("NOT VALID")  
            print("NOT VALID")  
            break

    with open('mySolutions/solution_' + X + '_' + YZ, 'w') as f:
        if(valid):    
            print("GOOD PLAN")
            print(" VALID")  
            f.write('GOOD PLAN')
        else:
            print("BAD PLAN")
            f.write("BAD PLAN\n")
            #print('\n', myDict, '\n')
            for item in myDict:
                # print missed squares 
                if myDict[item] == 'open':          
                    print(item[1],", ", item[0]) 
                    f.write(str(item[1]) + ", " + str(item[0]) + '\n')

    f.close()

def write_solution_without_S(openElements):

    with open('mySolutions/solution_' + X + '_' + YZ, 'w') as f:
        if(not openElements):    
            #print("GOOD PLAN")
            f.write('GOOD PLAN')
        else:
            #print("BAD PLAN")
            f.write("BAD PLAN\n")

            for item in openElements:
                # print missed squares 
                print(item[1],", ", item[0]) 
                f.write(str(item[1]) + ", " + str(item[0]) + '\n')



def checkPlan(emptySquares, agent):
    newCoord = []
    
    # Create an empty dictionary to hold all the emptySquares and agent position
    myDict = {}
    # Use a for loop to add the list to the dictionary with values set to 'open'
    for item in emptySquares:
        myDict[item] = 'open'
    myDict[tuple(agent)] = 'visited' 
    
    for char in proposedAns:
        if char == 'N':
            newCoord = goNorth(agent.copy())
        if char == 'S':
            newCoord = goSouth(agent.copy())
        if char == 'E':
            newCoord = goEast(agent.copy())
        if char == 'W':
            newCoord = goWest(agent.copy())

        if tuple(newCoord) in emptySquares: 
            agent = newCoord
            myDict[tuple(newCoord)] = 'visited'

    return(myDict)

    
def checkPlanNoS(emptySquares):
    openElements = []
    for item in emptySquares[:-1]:
        agent = list(item) 
        dictNoS = checkPlan(emptySquares[:-1], agent)
        
        for item in dictNoS:
        # print missed squares 
            if dictNoS[item] == 'open': 
                openElements.append(item)

    unique_set = set(openElements)
    # Convert the set back to a list
    unique_list = list(unique_set)
    return(unique_list)


def is_valid_move_dfs(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'X' and (x, y) not in visited

def get_direction(current, next_pos):
    x_curr, y_curr = current
    x_next, y_next = next_pos

    if x_next == x_curr + 1:
        return 'N'
    elif x_next == x_curr - 1:
        return 'S'
    elif y_next == y_curr + 1:
        return 'W'
    elif y_next == y_curr - 1:
        return 'E'

def dfs(maze, current_position, goal, visited, path):
    x, y = current_position

    if current_position == goal:
        path.append(current_position)
        return True

    visited.add(current_position)
    
    for neighbor in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if is_valid_move_dfs(maze, *neighbor, visited):
            if dfs(maze, neighbor, goal, visited, path):
                path.append(current_position)
                return True

    return False



def find_solution_with_S(plan):
    with open('mySolutions/solution_' + X + '_' + YZ, 'w') as f:
        if plan:
            f.write(''.join(plan))
        else:
            f.write('BAD PLAN\n') 




def find_path_dfs(maze, start):
    empty_positions = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == ' ']

    visited_set = set()
    path = []
    all_paths_coordinates = []

    for goal in empty_positions:
        if not dfs(maze, start, goal, visited_set, path):
            print("No path found to goal at", goal)
            return

        path_coordinates = [get_direction(path[i], path[i + 1]) for i in range(len(path) - 1)]
        path_coordinates_str = ''.join(path_coordinates[::-1])

        print("\nPath found to goal at", goal, "as coordinates:", path_coordinates_str)
        print("Path found to goal at", goal, "as coordinates (full):", path[::-1])

        # Write the solution to a file
        find_solution_with_S(path_coordinates_str)

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


#__MAIN__

# Open the file for reading
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    l = filename.split("_")
    X = l[1]
    YZ = l[2]

    if X == 'e' or X == 'f':
        break
    else:
        with open(workingFolder + '\\' + filename, 'r') as file2:
            # Read the first line
            line = file2.readlines()
            _map = [item.replace('\n', "") for item in line]
            
            # Extract the first line (type of the problem)
            problemType = _map[0]
            #print(problemType)
            if problemType == "CHECK PLAN": 
                # Extract the second line (solution of the problem)
                proposedAns = _map[1]
                cave = _map[2:]
                emptySquares, agent = find_mapElements(cave)
                if agent:  
                    finalDict = checkPlan(emptySquares.copy(), agent.copy())
                    write_solution_with_S(finalDict)
                else:
                    finalList = checkPlanNoS(emptySquares.copy())
                    write_solution_without_S(finalList)
                    
                
            if problemType == "FIND PLAN": 
                sample_maze = _map[1:]
                _ , agent = find_mapElements(sample_maze)
                path_dfs = find_path_dfs(sample_maze, tuple(agent))
                #print("Find")
          
                # findPlan()
            
