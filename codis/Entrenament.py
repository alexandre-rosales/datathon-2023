from General import obtenir_estructura
import numpy as np
from scipy.optimize import minimize
from time import time

def distancia(p1, p2):
    return np.linalg.norm(p1 - p2)

def objective_function(positions):
    total_error = 0.0

    for peca in peces:
        for adj in peca.adjacents:
            if adj < 1000:
                actual_distance = distancia(positions[peca.n], positions[adj])
                desired_distance = peca.distancia(peces[adj])
                error = (actual_distance - desired_distance) ** 2
                total_error += error

    return total_error

def optimize_positions(n, d):
    initial_positions = np.random.rand(n, d)  # Initialize positions randomly

    result = minimize(objective_function, initial_positions,
                      method='L-BFGS-B', options={'disp': True})

    optimized_positions = result.x.reshape((n, d))
    return optimized_positions

# Example usage:
outfits, peca, peces = obtenir_estructura(1,255)
peces = peces[:1000]
d = 2
t0 = time()
optimized_positions = optimize_positions(len(peces), d)
dt = time()-t0
print("Optimized positions:\n", optimized_positions)
print(dt)
