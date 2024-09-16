import random

def create_initial_state(n):
    # Place one queen in each column randomly
    return [random.randint(0, n - 1) for _ in range(n)]

def count_attacking_pairs(state):
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    for col in range(len(state)):
        for row in range(len(state)):
            if row != state[col]:
                neighbor = state[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def k_beams(n, k, max_iterations):
    # Initialize K random configurations (beams)
    beams = [create_initial_state(n) for _ in range(k)]
    
    for iteration in range(max_iterations):
        new_beams = []
        for beam in beams:
            neighbors = get_neighbors(beam)
            # Evaluate neighbors and sort them by the number of attacking pairs
            neighbors.sort(key=lambda state: count_attacking_pairs(state))
            # Take the top K neighbors
            new_beams.extend(neighbors[:k])
        
        # Keep only the top K beams
        new_beams.sort(key=lambda state: count_attacking_pairs(state))
        beams = new_beams[:k]
        
        # Check if we have found a solution
        for beam in beams:
            if count_attacking_pairs(beam) == 0:
                return beam
    
    return None  # No solution found within the given number of iterations

n = 8  # Example for 8-Queens problem
k = 100  # Number of beams
max_iterations = 1000  # Number of iterations to run

solution = k_beams(n, k, max_iterations)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")
