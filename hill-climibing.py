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

def hill_climbing(n):
    current_state = create_initial_state(n)
    current_score = count_attacking_pairs(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=lambda state: count_attacking_pairs(state))
        next_score = count_attacking_pairs(next_state)
        
        if next_score >= current_score:
            break
        current_state, current_score = next_state, next_score
    
    if current_score == 0:
        return current_state
    else:
        return None  # No solution found

n = 8  # Example for 8-Queens problem
solution = hill_climbing(n)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")
