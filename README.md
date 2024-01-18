# Assignment 1.0: Wumpus-Cave

This repository contains a Python implementation that serves as a solver for the Wumpus World problem, involving a grid-based environment where an agent (vacuum cleaner) needs to navigate, following a sequence of instructions, to clean the entire area. The code provides a detailed solution, including tracking the agent's movement and validating the cleaning plan.



## Table of Contents

- [Introduction](#introduction)
  - Key Features
- [Setup](#setup)
  - Repository content
  - How to run the code
  - Used libraries
- [Code Structure](#code-structure)
- [Self Evaluation and Design Decisions](#design-decision)

## Introduction
In the realm of Wumpus World, an agent, akin to a virtual explorer, must traverse through a grid. The "CHECK PLAN" problem type involves scrutinizing whether a proposed sequence of movements and actions ensures the agent's successful coverage of the entire area, factoring in its initial position.

Key features of this script include functions to simulate cardinal movements (North, South, East, West), identify the location of empty squares, and validate the proposed plan's efficacy. The script meticulously documents the results, generating insightful reports on the plan's success or pinpointing any squares that may have been overlooked.

### Key Features 

- **Movement Simulation:** The script provides functions to simulate the movement of the agent in different directions (North, South, East, West).

- **Mapping Elements:** It identifies the coordinates of empty squares and the starting position of the agent within the grid.

- **Plan Validation:** The script checks whether a proposed plan effectively cleans the entire area, considering the starting position of the agent. It produces a detailed report of the plan's validity.

- **File Output:** The script generates solution files that document the outcome of the plan, indicating whether it is successful or identifying any potentially missed squares.

- **Automation:** It can process multiple problem files within a specified directory, automating the solution generation for a batch of Wumpus World scenarios.

## Setup
### This repository contains:
 1) **`wumpus.py`**:
 2) **`mySolutions`**: Folder that contains the solutions for the 'problems'.

### How to run the code: 
1) import os
2) **`wumpus.py`** and **problems** folder should be on the same folder
3) A **mySolutions** folder must be created if not existed in the same folder with **`wumpus.py`**
4) Run **`wumpus.py`** 

### Used libraries:
**_os:_**
The os module provides a portable way to use operating system-dependent functionality, such as reading or writing to the file system, manipulating the file paths, working with environment variables, and executing system commands.

## Code Structure
### **■ Library imports:**
```python
import os
```
### **■ Global Variables:**
```python
workingFolder = "problems"
directory = os.fsencode(workingFolder)
```
- Global variables are defined to set the working folder and create a directory object using the 'os.fsencode' function.

### **■ Direction Functions:**

```python
def goNorth(agent):
    # ...

def goSouth(agent):
    # ...

def goWest(agent):
    # ...

def goEast(agent):
    # ...
```
- Each of those functions Simulates moving the vacuum cleaner/agent one square in the cardinal directions.
- Handles boundary conditions by wrapping around to the opposite side if needed.

### **■ Extract Map Elements:**

```python
   def find_mapElements(_map):
    # ...
```
- Finds and returns the coordinates of empty squares and the starting position of the vacuum cleaner in the given map.
- Takes as a parameter: `_map` List of strings representing the Wumpus cave.
- Returns: 
    - `emptySquares` (list of tuples): A list containing the coordinates of empty squares in the grid.
    - `agent` (list): The initial position of the agent in the grid represented as a list of [y, x] coordinates.

### **■ Check Plane With S:**
```python
def checkPlan(emptySquares, agent):
    # ...
```
- Takes as parameters the coordinates of empty squares in the grid and the agent starting position
- Returns a dictionary (myDict) where keys are tuples representing coordinates of squares in the grid, and values indicate the status of each square after executing the plan ('open' for unvisited squares and 'visited' for visited squares).

**1) Initialize an Empty Dictionary (myDict):**
```python
myDict = {}
```
- Create an empty dictionary to store the status of each square in the grid.

**2) Populate Dictionary with Empty Squares:**
```python
for item in emptySquares:
    myDict[item] = 'open'
```
- Use a for loop to populate the dictionary with the empty squares from the emptySquares list. Set the initial status for all squares to 'open'.


**3) Set Agent's Initial Position as Visited:**
```python
myDict[tuple(agent)] = 'visited'
```
- Set the initial position of the agent in the dictionary to 'visited'.


**4) Iterate Through the Proposed Plan:**
```python
for char in proposedAns:
```
- Use a for loop to iterate through each character in the global variable proposedAns, which represents the proposed plan of movement.


**5) Simulate Movement Based on Plan:**
```python
if char == 'N':
    newCoord = goNorth(agent.copy())
if char == 'S':
    newCoord = goSouth(agent.copy())
if char == 'E':
    newCoord = goEast(agent.copy())
if char == 'W':
    newCoord = goWest(agent.copy())
```
- Based on the character in the proposed plan (char), simulate the agent's movement in the grid using directional functions (goNorth, goSouth, goEast, goWest).
- Update the agent's position (newCoord) based on the movement.


**6) Check Validity of New Position:**
```python
if tuple(newCoord) in emptySquares:
    agent = newCoord
    myDict[tuple(newCoord)] = 'visited'
```
- Check if the new position (newCoord) is within the list of empty squares (emptySquares).
If the new position is valid, update the agent's position and set the corresponding square in the dictionary to 'visited'.


**7) Return the Final Dictionary:**
```python
return myDict
```
- After simulating the entire plan, return the final dictionary (myDict) indicating the status of each square in the grid.


### **■ write_solution_with_S(myDict):**
- Writes the solution to a file, indicating whether the plan is valid or not when the starting position is specified.
- Takes the return of `checkPlan(emptySquares, agent)` which is `myDict`: A dictionary indicating the status of each square in the Wumpus cave.
```python
finalDict = checkPlan(emptySquares.copy(), agent.copy())
write_solution_with_S(finalDict)
```


### **■ Check Plan (No Starting Position) Function:**
- Takes as parameters the coordinates of empty squares in the grid as a parameter
```python
dictNoS = checkPlan(emptySquares[:-1], agent)
```
- The checkPlanNoS function iterates through different starting positions to check plans within a grid-based environment without a specified starting position. It calls the checkPlan function for each starting position, allowing it to simulate movement and validate proposed plans. The function returns a list of potentially missed squares in the grid.

**1) Initialize an Empty List (openElements):**
```python
openElements = []
```
- Create an empty list to store potentially missed squares in the grid.

**2) Iterate Through Different Starting Positions:**
```python
for item in emptySquares[:-1]:
```
- Use a for loop to iterate through each item in the emptySquares list (excluding the last item, which represents the starting position).

**3) Convert Tuple to List (agent):**
```python
agent = list(item)
```
- Convert the tuple item to a list (agent) to use as the starting position.

**4) Call checkPlan for Each Starting Position:**
- Call the checkPlan function with the current starting position (agent) and the list of empty squares  `emptySquares[:-1]` (excluding the last item, which represents the starting position)
```python
dictNoS = checkPlan(emptySquares[:-1], agent)
```

**5) Identify Potentially Missed Squares:**
```python
for item in dictNoS:
    if dictNoS[item] == 'open':
        openElements.append(item)
```
- Iterate through the dictionary (dictNoS) obtained from calling checkPlan to identify squares marked as 'open' (potentially missed squares).

**6) Remove Duplicates from List (openElements):**
```python
unique_set = set(openElements)
unique_list = list(unique_set)
```
Remove duplicate entries from the list of potentially missed squares.

**7) Return the List of Potentially Missed Squares:**
```python
return unique_list
```
- Return the final list of potentially missed squares in the grid.

### **■ write_solution_with_S(myDict):**
- Writes the solution to a file, indicating whether the plan is valid or not when starting position variations are considered.
- Takes the return of `checkPlanNoS(emptySquares)` which is `unique_list`: A list of potentially missed squares when starting position variations are considered.
```python
finalList = checkPlanNoS(emptySquares.copy())
write_solution_without_S(finalList)
```

## Self Evaluation and Design Decisions
- **Directional Movement Functions:** Functions like goNorth, goSouth, goWest, and goEast facilitate movement within the grid by adjusting coordinates based on cardinal directions.
- **Map Element Identification:** The find_mapElements function identifies empty squares and the agent's position in the grid, providing essential information for subsequent analysis.
- **Handling Starting Positions:** The script accommodates both specified and unspecified starting positions, addressing the challenge of dynamic plan checking.
- **Plan Validation and Reporting:** Functions like checkPlan and checkPlanNoS validate plans, mark visited squares, and report on the plan's validity or potential missed squares.
- **File Output:** The script writes solutions to files, indicating whether the plan is valid or detailing missed squares.

**SCORE:** <br />

<img width="152" alt="image" src="https://github.com/BassemMagdi0007/Wumpus-Cave/assets/60258792/1d50ccaa-71a4-4259-b3fb-dd3c25c86c1b">

- The Code successfully scores 10 points for each of a,b and c problems of the example-problems 

