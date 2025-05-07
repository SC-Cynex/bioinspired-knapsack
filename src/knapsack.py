import numpy as np

def fitness(individual, values, weights, capacity):
    total_weight = np.dot(individual, weights)
    if total_weight > capacity:
        return 0
    return np.dot(individual, values)

def generate_individual(n):
    return np.random.randint(2, size=n)

def generate_population(pop_size, n):
    return [generate_individual(n) for _ in range(pop_size)]
