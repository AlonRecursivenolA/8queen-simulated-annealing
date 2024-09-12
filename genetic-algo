import random

def fitness(board):
    non_attacking_pairs = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = n // 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(board, mutation_probability):
    if random.random() < mutation_probability:
        i, j = random.sample(range(len(board)), 2)
        board[i], board[j] = board[j], board[i]
    return board

def genetic_algorithm(n, population_size, mutation_probability, generations):
    population = [random.sample(range(n), n) for _ in range(population_size)]
    
    for generation in range(generations):
        fitness_scores = [fitness(board) for board in population]
        
        if max(fitness_scores) == (n * (n - 1)) // 2:
            print("Solution found!")
            break
        
        parents = random.choices(population, k=population_size)
        
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = parents[i], parents[i+1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_probability))
            new_population.append(mutate(child2, mutation_probability))
        
        population = new_population
    
    best_board = max(population, key=fitness)
    return best_board

n = 8
population_size = 100
mutation_probability = 0.01
generations = 1000
solution = genetic_algorithm(n, population_size, mutation_probability, generations)
print("Best Board Configuration:", solution)
